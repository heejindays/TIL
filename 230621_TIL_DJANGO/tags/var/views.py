from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "var/index.html")

def variable01(request):
    # 리스트 값을 만들어서 탭플릿으로 전달
    my_list = ["python", "django"]
    return render(request, "var/variable01.html", {"lst": my_list})