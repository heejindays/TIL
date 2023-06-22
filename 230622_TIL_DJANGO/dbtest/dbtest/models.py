from django.db import models

class MyBoard(models.Model):
    # models에 파이썬 클래스를 만들었음
    # 속성 4개를 만들어서 CharField를 사용해서 문자열 필드를 만듦
    # 마이보드 클래스가 모델 객체가 됨
    myname = models.CharField(max_length=100)
    mytitle = models.CharField(max_length=500)
    mycontent = models.CharField(max_length=2000)
    mydate = models.DateTimeField()
