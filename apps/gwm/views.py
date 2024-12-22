from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.conf import settings
from django.db.models import Case, When, BooleanField
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Apk
from .handler import insert_or_update_apk, collect_apk_files
import logging
import json
import os
import uuid

logger = logging.getLogger(__name__)


def home(request):
    return redirect(reverse('apps.gwm:gwm_h6'))


def gwm_h6(request):
    current_dns = os.environ.get('ENTRY_IP', 'Unknown')
    page_limit = settings.PAGINATE_BY
    # apk_list = Apk.objects.order_by('locked').order_by('-modify_at')
    apk_list = Apk.objects.annotate(
            is_locked=Case(
                When(locked=True, then=True),
                default=False,
                output_field=BooleanField()
            )
        ).order_by('-is_locked', '-modify_at')
    paginator = Paginator(apk_list, page_limit)
    page = request.GET.get('page')
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)
    return render(request, 'gwm/h6.html', locals())


def add_apk(request):
    json_data = {'code': 1000}
    if request.method == "POST":
        request_body_dict = json.loads(request.body)
        print(request_body_dict)
        insert_or_update_apk(request_body_dict)  # noqa: F405
        json_data['message'] = 'ok'
        return JsonResponse(json_data, status=200)
    new_apk_id = uuid.uuid4()
    add_apk_tpl = loader.render_to_string(
        'gwm/_modal_add_apk.html',
        {
            'new_apk_id': new_apk_id
        }
    )
    json_data['modal_context'] = add_apk_tpl
    return JsonResponse(json_data, status=200)


@login_required
@user_passes_test(lambda x: x.is_superuser)
def set_current_ota(request):
    apk_id = request.GET.get('apk_id')
    json_data = {'code': 1000}
    try:
        apk = Apk.objects.get(pk=apk_id)
        if apk.locked:
            apk.locked = False
            json_data['message'] = "False"
        else:
            apk.locked = True
            json_data['message'] = "True"
        apk.save()
    except Apk.DoesNotExist:
        logger.warning("the apk is not existed")
        json_data = {'code': 1002, 'message': "apk not found."}
    return JsonResponse(status=200, data=json_data)


def search_apk(request):
    json_data = {"code": 1006}
    if request.method == "POST":
        name_keyword = str(request.POST.get('keyword')).strip()
        selected_apk_list = Apk.objects.filter(name__icontains=name_keyword)
        selected_user_list_html = loader.render_to_string(
            'gwm/_table_h6_apk_list.html',
            {'items': selected_apk_list}
        )
        json_data = {
            "code": 1000,
            "amount": selected_apk_list.count(),
            "item_list": selected_user_list_html
        }
        return JsonResponse(status=200, data=json_data)
    return JsonResponse(status=405, data=json_data)


def find_apks(request):
    json_data = {'code': 1000}
    apk_list = collect_apk_files()
    logger.info(f'find local apks list: {apk_list}')
    for apk in apk_list:
        val = {}
        val['id'] = apk['id']
        val['name'] = apk['name']
        val['file_url'] = apk['url']
        val['file_md5'] = apk['md5']
        val['file_size'] = apk['size']
        val['comment'] = "local file."
        insert_or_update_apk(val)
    json_data['file_count'] = len(apk_list)
    return JsonResponse(status=200, data=json_data)


def h6_apk_update(request):
    locked_apk = Apk.objects.filter(locked=True, status="public").first()
    if not locked_apk:
        json_data = {
            "code": 200,
            "message": "Query OK. APK download url unconfigured or unlocked.",
            "data": ""
        }
    else:
        h6_callback = loader.render_to_string(
            'gwm/h6_callback.json.tpl',
            {'apk': locked_apk}
        )
        json_data = json.loads(h6_callback)
    return JsonResponse(status=200, data=json_data)
