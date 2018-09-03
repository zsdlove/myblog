from django.shortcuts import render
from django.shortcuts import HttpResponse
from zsdlove import models
from markdown import markdown
from zsdlove.models import Blog,Tag,Category,friend_link,public_notice
# Create your views here.
employee_list=[
    {"id":"1","name":"zsdlove"},
    {"id":"2","name":"liudehua"},
    {"id":"3","name":"zhangxueyou"}
]
def index(request):
        return render(request,"index.html")
def login(request):
        if request.method=='POST':
            username=request.POST.get("username",None)
            password=request.POST.get("password",None)
            if username=="zsdlove" and password=="zsdlove":
                print("登陆成功")
                return render(request,'success.html',{"data":employee_list})
            else:
                print("登陆失败")
        return render(request,'login.html')
def add(request):
        if request.method=='POST':
            employee_id=request.POST.get("employee_id",None)
            employee_name=request.POST.get("employee_name",None)
            models.employeeInfo.objects.create(emploee_id=employee_id,emploee_name=employee_name)
        employee_list=models.employeeInfo.objects.all()
        return render(request,'add.html',{"data":employee_list})

def delete(request):
    if request.method == 'GET':# daxie
        emploee_name = request.GET.get("emploee_name")
        print("打印"+emploee_name)
        models.employeeInfo.objects.filter(emploee_name=emploee_name).delete()
    employee_list = models.employeeInfo.objects.all()
    return render(request, 'add.html', {"data": employee_list})

def blogindex(request):
    all_blog=Blog.objects.all().order_by('-id')
    all_friend_link=friend_link.objects.all()
    notice=public_notice.objects.get(notice_id='1')
    return render(request,"blog-tp/index.html",{'all_blog':all_blog,'all_friend_link':all_friend_link,'notice':notice})
def article_detail(request):
    blog_id=request.GET.get("blog_id")
    print(blog_id)
    blog = Blog.objects.get(id=blog_id)
    blog.content=markdown(blog.content)
    return  render(request,"blog-tp/article_detail.html",{"blog":blog},)
def comment(request):

    return render(request,"blog-tp/comment.html")