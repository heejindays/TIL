from django.shortcuts import render

def index(request):
    return render(request, "tags/index.html", {"name":"heejin"})
# 요청 받은 걸 템플릿 레이어에 전달 "tags/index.html"
# {"name":"heejin"}의 값을 가지고 갈 것이다