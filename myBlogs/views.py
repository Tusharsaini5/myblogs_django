from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import blog_category, contact_info, blog_post, comment
from .form import Blog_Form, BlogPost_Form
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
# Create your views here.

def home(request):
    # return HttpResponse('<h1>this is the home page</h1>')
    #fetch the data from db
    x=blog_category.objects.all()
    # print (x)
    return render(request, 'myBlogs/home.html',{"category":x})


def contact(request):
    # return HttpResponse('<h1>this is the contact page</h1>')
    if request.method == 'GET':
        return render(request, 'myBlogs/contact.html')
    elif request.method == 'POST':
        email = request.POST.get('user_email')
        message = request.POST.get('message')
        x = contact_info(u_email=email, u_message=message)
        x.save()
        print(email)
        print(message)
        return render(request,'myBlogs/contact.html',{'feedback':'Your message has been recorded'})


@login_required(login_url='loginuser')
def blog(request):
    x = Blog_Form()  
    if request.method == "GET":
        return render(request,'myBlogs/blog.html',{"x":x})
    else:
        print("hi")
        form = Blog_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print("hi")
            return redirect('home')
        else:
            return render(request,'myBlogs/blog.html',{"x":x})


def ck(request):
    x = BlogPost_Form()
    return render(request,'myBlogs/ck.html',{"x":x})


def allblogs(request):
    x = blog_post.objects.all()
    var = request.GET.get('category')
    print(var)
    if(var):
        x=blog_post.objects.filter(Blog_cat__blog_cat=var)
        print(x)
    else:
        x=blog_post.objects.all()
        print(x)

    p = Paginator(x, 3)
    page_number = request.GET.get("page")
    page_obj = p.get_page(page_number)
    return render(request,'myBlogs/allblogs.html',{"y":x})
    

def blog_details(request, blog_id):
    obj = get_object_or_404(blog_post, pk=blog_id)
    z=obj.view_count
    z=z+1
    obj.view_count=z
    obj.save()
    # if request.method == 'GET':
    #     return HttpResponse(href='{% url 'add_comment' obj.blog_name %}?blog_id={obj.id}')
    # print(obj)
    # print(blog_id)
    
    return render(request,'myblogs/blog_details.html', {"obj":obj})


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'myBlogs/loginuser.html', {'form':AuthenticationForm()})
    else:
        a = request.POST.get('username')
        b = request.POST.get('password')
        user = authenticate(request, username=a, password=b)
        if user is None:
            return render(request, 'myBlogs/loginuser.html', {'form': AuthenticationForm(), 'error': 'Invalid Credintials'})
        else:
            login(request,user)
            return redirect('home')


def signupuser(request):
    if request.method == 'GET':
        return render(request, 'myBlogs/signupuser.html', {'form':UserCreationForm()})
    else:
        a=request.POST.get('username')
        b=request.POST.get('password1')
        c=request.POST.get('password2')
        if b==c:
            if(User.objects.filter(username =a)):
                return render(request,'myBlogs/signupuser.html', {'form':UserCreationForm(), 'error': 'Username already in exist. Try diffrent username'})
            else:
                user = User.objects.create_user(username=a, password=b)
                user.save()
                login(request,user)
                return redirect('home')
        else:
            return render(request,'myBlogs/signupuser.html', {'form':UserCreationForm(), 'error': 'Password Mismatch Try Again'})


def logoutuser(request):
    if request.method == 'GET':
        logout(request)
        return redirect('home')


def cat_blog(request):
    category_name = request.GET.get('category')
    if category_name:
        blogs = blog_post.objects,filter(blog_cat= category_name)
    else:
        blogs = blog_post.objects.all()
        return render(request,'my_Blog/allblogs.html',{"blogs":blogs,"category":category_name})


def find_blog(request):
    if(request.method == 'POST'):
        x = request.POST.get('blog_search')
        print(x)
        mydata = blog_category.objects.filter(Q(blog_cat__icontains=x))
        mydata2 = blog_post.objects.filter(blog_title__icontains=x)  
        return render(request, 'myBlogs/allblogs.html',{"y":mydata2})


def add_like(request,blog_id):
    obj = get_object_or_404(blog_post, pk=blog_id)
    y = obj.like_count
    y = y+1
    obj.like_count = y
    obj.save()
    return redirect('blog_details',obj.id)


def add_comment(request,blog_title):
    Blog_id=request.GET.get('blog_id')
    print(Blog_id)
    c_obj=comment.objects.all()
    print(c_obj)
    obj=get_object_or_404(blog_post, pk=Blog_id)
    if(request.method == 'GET'):
        redirect('home')
        return render(request,'myblogs/blog_details.html', {"obj":obj, "c_obj":c_obj})
    elif(request.method == 'POST'):
        x = request.POST.get('comment')
        print(x)
        # obj2=comment
        # obj2.comment_info=x
        # obj2.comment_email=request.user.email
        # obj2.comment_id=blog_title
        # title= str(blog_title)

        obj2 = comment(comment_email=str(request.user.email), comment_info=str(x), comment_id=obj )    
        # print(obj2.comment_email)
        obj2.save()

        return render(request,'myblogs/blog_details.html', {"obj":obj, "c_obj":c_obj})
    
    return render(request,'myblogs/blog_details.html', {"obj":obj, "c_obj":c_obj})