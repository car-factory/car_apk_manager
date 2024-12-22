"""
URL configuration for car_apk_manager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include
from apps.gwm import views as gwm_views

admin.site.site_title = 'CarApkManager'
admin.site.site_header = 'CarApkManagerAdmin'
admin.site.site_url= '/gwm/h6'

urlpatterns = [
    path("dash/2024/", admin.site.urls),
    re_path(r'^$', gwm_views.home, name='home'),

    re_path(r'^gwm/', include('apps.gwm.urls')),

    # factory motor api
    re_path("apiv2/car_apk_update$", gwm_views.h6_apk_update, name='gwm_h6_apk_update'),
]
