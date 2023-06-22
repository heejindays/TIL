from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1><a href='/hello01/test'>Hello, Django</a></h1>")


def test(request):
    return HttpResponse("<h1><a href='/hello01'>Bye, Django</a></h1>")

# https://docs.djangoproject.com/en/4.2/topics/templates/ 복습할 때 이 페이지 확인하기