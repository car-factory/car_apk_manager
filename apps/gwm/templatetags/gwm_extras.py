# -*- coding:utf-8 -*-

from django import template
from urllib.parse import urlencode
# from django.urls import Resolver404, resolve
from django.utils.safestring import mark_safe
# from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
def bool_to_yes_no(value):
    if value:
        return "Yes"
    else:
        return "No"


@register.filter("major_check")
def major_check(status):
    tpl = """
    <i class="bi-{}" style="font-size:13px;color:{};font-weight:500"></i>"""
    if status:
        status_html = tpl.format("check-circle-fill", "#3780eb")
    else:
        status_html = tpl.format("x-circle-fill", "#ff4f4f")
    return mark_safe(status_html)


@register.simple_tag(takes_context=True)
def current_query_string(context, **kwargs):
    """
    ref:
    https://github.com/harvard-lil/perma/blob/develop/perma_web/perma/templatetags/current_query_string.py
    """
    query_params = dict(context['request'].GET, **kwargs)
    query_params.pop('page', None)
    current_query_params = urlencode(query_params, doseq=True)
    if current_query_params:
        current_query_params = "&" + current_query_params
    return current_query_params
