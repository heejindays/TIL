from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    # 아무것도 안 붙으면 나랑 같은 페이지에 있는 views로 처리한다
    path("var01/", views.variable01),
]