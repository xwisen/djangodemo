from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse
from django.shortcuts import render

class PingViews():
    def __init__(self):
        pass
    def ping(request):
        return HttpResponse("It's OK !")
    def index(request):
        # 默认渲染的时候会去项目的templates 下寻找; setting.py TEMPLATES 变量设置
        # index.html 里面有引用js时，会加上/index前缀
        return render(request, "index.html")
