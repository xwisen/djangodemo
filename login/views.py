from django.shortcuts import render

# Create your views here.

from django.shortcuts import HttpResponse
from django.shortcuts import render

from login import models

class LoginViews():
    def __init__(self):
        pass
    def login(request):
        # 默认渲染的时候会去项目的templates 下寻找; setting.py TEMPLATES 变量设置
        # index.html 里面有引用js时，会加上/index前缀
        user_list = []
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            # 将数据保存到数据库
            models.UserInfo.objects.create(username=username, password=password)

            # 从数据库中读取所有数据，注意缩进
        user_list = models.UserInfo.objects.all()
        return render(request, 'login.html', {'data': user_list})

if __name__ == '__main__':
    pass