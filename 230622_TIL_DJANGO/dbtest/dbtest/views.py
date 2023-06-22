from django.shortcuts import render, redirect
from .models import MyBoard
from django.utils import timezone

def index(request):
    return render(request, "index.html", {"list": MyBoard.objects.all()})
    # MyBoard.objects.all() == select * from dbtest_myboard;
    # 그 테이블의 모든 데이터를 가지고 오고 싶다
    # 테이블을 파이썬 MyBoard 객체로 바꿈

def detail(request, id):
    dto = MyBoard.objects.get(id=id)
    return render(request, "detail.html", {"dto": dto})

def insert_form(request):
    return render(request, "insert.html")

def insert_res(request):
    myname = request.POST['myname']
    mytitle = request.POST['mytitle']
    mycontent = request.POST['mycontent']
    result = MyBoard.objects.create(myname=myname, mytitle=mytitle, mycontent=mycontent, mydate=timezone.now())

    if result:
        return redirect("index")
    else:
        return redirect("insertform")

    # (기본) 클라이언트가 서버에 요청한다 서버는 처리 후 클라이언트에게 응답한다
    # 리퀘스트랑 리스판스는 객체

    # (리다이렉트) 서버가 클라이언트한테 응답하다가 다시 요청한다
    # 리다이렉트를 하면 서버에서 클라이언트로 일단 나간 다음에 리스판스 객체가 만들어지는데
    # 클라이언트한테 닿기 전에 다시 요청함 (그 과정에서 새로운 객체가 만들어짐)
