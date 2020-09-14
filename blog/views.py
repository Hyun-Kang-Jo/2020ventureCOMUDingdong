from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .models import Blog

# Create your views here.

def home(request):
    blogs = Blog.objects
    return render(request, 'home.html', {'blogs':blogs})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)#Blog 모델명
    return render(request, 'detail.html', {'blog_detail':blog_detail})

def write(request):
    return render(request, 'write.html')

def send(request):
    blog = Blog()
    blog.title = request.POST['title']
    blog.body = request.POST['body']
    blog.pub_date = timezone.datetime.now()
    blog.image = request.FILES['image']
    blog.description = request.POST['description']
    blog.save()
    return redirect('/blog/' + str(blog.id))

def delete(request, blog_id):
    blog_delete = get_object_or_404(Blog, pk=blog_id)
    blog_delete.delete()
    return redirect('home')

def update(request, blog_id):
    blog_update = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'update.html', {'blog_update':blog_update})

def updateSend(request, blog_id):
    updateSendBlog = get_object_or_404(Blog, pk=blog_id)
    updateSendBlog.title = request.GET['updateTitle']
    updateSendBlog.body = request.GET['updatebody']
    updateSendBlog.pub_date = timezone.datetime.now()
    updateSendBlog.save()
    return redirect('home')
