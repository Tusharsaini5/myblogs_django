"""
URL configuration for project1 project.

The urlpatterns list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from myBlogs import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('contact',views.contact,name='contact'),
    path('blog',views.blog,name='blog'),
    path('ck',views.ck,name='ck'),
    path('blog_post',views.blog_post,name='blog_post'),
    path('blog_category',views.blog_category,name='blog_category'),
    path('allblogs',views.allblogs,name='allblogs'),
    path('blog_details/<str:blog_id>/',views.blog_details,name ='blog_details'),
    path('loginuser',views.loginuser,name='loginuser'),
    path('signupuser',views.signupuser,name='signupuser'),
    path('logoutuser',views.logoutuser,name='logoutuser'),
    path('find_blog',views.find_blog,name='find_blog'),
    path('add_like/<str:blog_id>',views.add_like,name='add_like'),
    path('add_comment/<str:blog_title>/',views.add_comment,name='add_comment'),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)