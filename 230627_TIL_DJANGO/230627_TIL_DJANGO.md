## 1) admin



```py
from django.contrib import admin
from .models import MyBoard, MyMember

admin.site.register(MyBoard)
admin.site.register(MyMember)
```



- 모델 객체 만들어둔 것을 사이트에서 관리할 수 있도록 연결
- admin.py 파일을 생성하고 모델을 등록하지 않으면
- 관리자 페이지에서 해당 모델을 편집할 수 없음
- admin.site.register() 함수 : 모델을 등록하면 관리자 페이지에서 해당 모델 편집 가능



## 2) pagination



- views.py에서 index 페이지 페이지를 나누고 싶을 때

  

```py
def index(request):

myboard = MyBoard.objects.all().order_by("-id")

# MyBoard 모델의 모든 객체를 가져와서
# id를 기준으로 큰 수부터 나오도록 내림차순 정렬 ("-id")

paginator = Paginator(myboard, 5)
# 페이지를 나눠서 paginator에 넣겠다
# myboard : 페이지네이션을 적용할 대상
# 5 : 한 페이지에 보여질 수

page_num = request.GET.get("page", "1")
# get 방식으로 요청 들어온 것 중에서
# page 라는 이름의 값을 가져와서 page_num에 넣겠다
# "1"은 기본값
# GET 방식으로 요청할 때 ?page=2 여기 들어가는 숫자
# 즉, 지금 페이지 번호

print(page_num)  # 19 (실제로 누른 페이지 수)
print(type(page_num))  # <class 'str'>

page_obj = paginator.get_page(page_num)
# 지금 페이지 숫자를 기준으로 object를 가져옴

print(type(page_obj))  
# <class 'django.core.paginator.Page'>
    
print(page_obj.count)
# <bound method Sequence.count of <Page 13 of 21>> 
#21페이지 중에 13페이지에 있다
   

print(page_obj.paginator.num_pages) # 21 (전체 페이지 수)
  
print(page_obj.paginator.page_range) # range(1, 22) (전체 페이지 수의 범위)

print(page_obj.has_next())  # True (지금 기준으로 다음 페이지가 있니? T/F)

print(page_obj.has_previous())  # True (지금 기준으로 이전 페이지가 있니? T/F)

try:
	print(page_obj.next_page_number())  # 14 (지금 페이지의 다음 페이지 번호)
	print(page_obj.previous_page_number())  # 12 (지금 페이지의 이전 페이지 번호)

except:
	pass  # (아무것도 안하고 그냥 넘어가기)

print(page_obj.start_index())  
# 61 (지금 페이지 안에 있는 모델 객체의 시작 인덱스 / 13페이지 (5*12)+1)

print(page_obj.end_index())  
# 65 (지금 페이지 안에 있는 모델 객체의 마지막 인덱스 / 13페이지 5*13)

return render(request, "index.html", {"list": page_obj})
# page_obj가 "list"라는 변수로 "index.html" 탬플릿에 전달됨
```



## 3) login / logout

- login : 암호화와 사용자 인증에 대한 적절한 보안 기법을 적용하는 것이 중요

```py
def login(request):
    if request.method == "GET":
        return render(request, "login.html")
        # get 요청이 들어오면 login.html 템플릿을 렌더링하여 사용자에게 로그인 폼을 보여줌

    else:
        myname = request.POST["myname"]
        mypassword = request.POST["mypassword"]
        # POST 요청이 들어오면, 폼에서 입력받은 사용자이름(myname)과 비밀번호(mypassword) 확인

        mymember = MyMember.objects.get(myname=myname)
        # MyMember모델에서 사용자 이름으로 해당 회원을 조회함

        if check_password(mypassword, mymember.mypassword):
            request.session["myname"] = mymember.myname
            # 회원의 비밀번호와 입력받은 비밀번호를 비교해서 일치하면
            # 세션에 사용자 이름을 저장하고 index 페이지로 리디렉션
            return redirect("index")
        else:
            return redirect("login")
```



- logout

- 로그아웃 과정에서 추가적인 로직이 필요한 경우 해당 로직을 추가 가능
- 예를 들어, 로그아웃 시 일부 데이터를 삭제하거나 
- 로그아웃 후에 특정 페이지로 리디렉션하는 등의 동작 추가 가능

- 안전하고 보안적인 로그아웃을 위해서는 추가적인 조치가 필요
- 보안 상의 고려사항을 유념하여 로그아웃 기능을 구현

```py
def logout(request):
    # 세션에서 사용자 이름을 삭제
    del request.session["myname"]
    return redirect("index")
```



## 4) file upload / download

-  upload :  파일 업로드 시 타입 설정 중요 enctype="multipart/form-data"

- 업로드 완료된 파일은 settings.py에서 설정해 둔 폴더에서 확인 가능 (media 파일)

  ```py
  # settings.py 파일에 추가해야 함
  # media files (예시)
  MEDIA_URL = "/media/"
  MEDIA_ROOT = BASE_DIR/"media"
  ```



- settings.py에 적어둔 것 처럼 MEDIA_ROOT에 저장

- upload_file.read() 업로드 파일을 읽어와서 

- ContentFile 객체로 만듦 > 그래야 저장할 수 있음

- 왜 read의 과정이 필요하냐면 풀어진 상태로 보낸 거니까 가져와서 다시 read해야 함

  ```py
  def upload_process(request):
  
      upload_file = request.FILES["uploadfile"]
      print(upload_file.name)
      print(type(upload_file))
  
      uploaded = default_storage.save(upload_file.name, ContentFile(upload_file.read()))
      print(uploaded)
      print(type(uploaded)) # <class 'str'>
  
      return render(request, "download.html", {"filename": uploaded})
  ```

  

- download는 upload의 과정을 거꾸로 진행한 것

  ```py
  def download_process(request, filename):
      response = HttpResponse(default_storage.open(filename).read(),
                              content_type='application/force-download')
  
      return response
  ```

  