"""
URL configuration for tags project.

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
from django.urls import path

from django.contrib import admin
from django.urls import path, include
from . import views

# ***** 프로젝트의 이름(tags)과 같아서 기본적으로 이 urls가 가장 먼저 실행됨

urlpatterns = [
    path("admin/", admin.site.urls),
    # "" : 뒤에 아무것도 없는 요청이니까 root로 넘어옴 > views.index로 가자
    path("", views.index),
    # var/요청을 다시 받으면 또 여기로 와서 아래를 연결해서 실행함 (반복적으로)
    path("var/", include("var.urls")),
    path("statics/", include("statics.urls")),
]
