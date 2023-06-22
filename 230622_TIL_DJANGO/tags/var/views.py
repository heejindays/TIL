from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, "var/index.html")

def variable01(request):
    # 리스트 값을 만들어서 탭플릿으로 전달
    my_list = ["python", "django"]
    return render(request, "var/variable01.html", {"lst": my_list})

def variable02(request):
    my_dict = {"class": "multi", "name": "heejin"}
    return render(request, "var/variable02.html", {"dct": my_dict})

def forloop(request):
    return render(request, "var/forloop.html", {"number": range(1, 11)})

def if01(request):
    return render(request, "var/if01.html", {"user": {"id": "heejin", "job": "student"}})

def if02(request):
    return render(request, "var/if02.html", {"role": "manager", "id": "heejin"})

def href(request):
    return render(request, "var/href.html")

def get_post(request):
    if request.method == "GET":
        return render(request, "var/get.html")
    elif request.method == "POST":
        return render(request, "var/post.html")
    else:
        return redirect("index")