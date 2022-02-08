from django.shortcuts import render,HttpResponse
from blog.models import Blog,Contact
import math
# Create your views here.
def home(request):
    # return HttpResponse("THis is home")
    return render(request,'home.html')

def blog(request):
    no_of_posts = 3
    page = request.GET.get('page')
    # print(request.GET)
    if page is None:
        page = 1
    else:
        page = int(page)
    # print(page)
    blogs = Blog.objects.all()
    length = len(blogs)
    blogs = blogs[((page-1)*no_of_posts):(page*no_of_posts)]
    if page>1:
        prev = page-1
    else:
        prev = None
    if page<math.ceil(length/no_of_posts):
        nxt = page+1
    else:
        nxt = None
    context = {'blogs' : blogs,'prev' : prev, 'nxt' : nxt}
    return render(request,'blog.html',context)

def search(request):
    return render(request,'search.html')
    
def blogpost(request,slug):
    blog = Blog.objects.filter(slug=slug).first()
    # print()
    context = {'blog':blog}
    return render(request,'blogpost.html',context)

def contact(request):
    context={'success':False}
    if request.method=='POST':
        name = request.POST.get("name")
        mail = request.POST.get("email")
        phone = request.POST.get("phone")
        desc = request.POST.get("desc")
        ins = Contact(name=name, mail=mail, phone=phone, desc=desc)
        ins.save()
        context={'success':True}
    return render(request,'contact.html',context)
