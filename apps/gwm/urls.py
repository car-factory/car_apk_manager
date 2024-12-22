# -*- coding:utf-8 -*-
from django.urls import re_path, path
from apps.gwm import views as gwm_views
from django.contrib.auth import views as auth_views

app_name = 'apps.gwm'

"""
gwm service endpoint.
"""
urlpatterns = [
    # gwm h6
    re_path(r"h6$", gwm_views.gwm_h6, name='gwm_h6'),
    re_path(r'h6/search$', gwm_views.search_apk, name='search_apk'),
    re_path(r'h6/add$', gwm_views.add_apk, name='add_apk'),
    re_path(r'h6/find$', gwm_views.find_apks, name='find_apks'),
    re_path(r'h6/current_ota/set$', gwm_views.set_current_ota, name='set_current_ota')
]
