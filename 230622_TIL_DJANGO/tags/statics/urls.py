from django.urls import path
from . import views
# 나랑 같은 위치에 있는 views라는 파일을 가져와서 사용

urlpatterns = [
    path("", views.index),

]