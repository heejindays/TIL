from django.urls import path
from . import views

urlpatterns = [
    # href = "{% url 'index' %}"
    # "" : 같은 페이지에 있는 views로 처리
    path("", views.index, name="index"),
    path("var01/", views.variable01),
    path("var02/", views.variable02),
    path("forloop/", views.forloop),
    path("if01/", views.if01),
    path("if02/", views.if02),
    path("href/", views.href),
    path("request/", views.get_post),
]