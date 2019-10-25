from django.shortcuts import render
from django.shortcuts import HttpResponse


# from app import models

# # Create your views here.
# user_list=[{'user':'jack','pwd':'abc'},{'user':'tom','pwd':'ABC'}]
#
# def index(request):
#     # return HttpResponse('hello word')
#     # return render(request,'index.html')
#     if request.method == 'POST':
#         username = request.POST.get('username', None)
#         password = request.POST.get('password', None)
#         # temp={'user':username,'pwd':password}
#         # user_list.append(temp)
#         models.UserInfo.objects.create(user=username,pwd=password)
#     user_list=models.UserInfo.objects.all()
#
#     return render(request, 'index.html',{'data':user_list})

# def index(request):
#     name = 'newo'
#     i = 10
#     l = [1, 2, 'a']
#     info = {'name': 'neo', 'age': 22}
#     b=True
#     class Person(object):
#         def __init__(self, name, age):
#             self.name = name
#             self.age = age
#     alex = Person('alex', 33)
#     egon= Person('egon', 22)
#     person_list = [alex, egon]
#     # return render(request, 'index.html', locals())
#     #过滤器
#     import datetime
#     now = datetime.datetime.now()
#     empty_list = []
#     str = 'hello word'
#     text = 'Django is a hight=level python web framework'
#     link = "<a href='#'>click</a>"
#     #模板标签
#     num = 90
#     return render(request, 'index.html', locals())
# def login(request):
#     if request.method=='POST':
#         return HttpResponse('ok')
#     return render(request, 'login.html')
list1 = []
def index(request):
    if request.method == 'POST':
        username=request.POST.get('user')
        password=request.POST.get('password')
        list1.append({'use':username,'password':password})
    return render(request,'index.html',{'data':list1})





# def  index (request) :
#     i = 10
#     return render(request, 'index.html', locals())
#
# def orders(request):
#     return render(request, 'orders.html')




