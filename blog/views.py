from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator

from .models import Blog, Photo

# Create your views here.

def home(request):
    blogs = Blog.objects
    #블로그 모든 글들을 대상으로
    blog_list=Blog.objects.all()
    #블로그 객체 세 개를 한 페이지로 자르기
    paginator = Paginator(blog_list,3)
    #request된 페이지가 뭔지 알고 request페이지를 변수에 담음
    page = request.GET.get('page')#html에서 온 값
    #request된 페이지를 얻어온 뒤 return 해 준다.
    posts = paginator.get_page(page)

    return render(request, 'home.html', {'blogs':blogs, 'posts':posts})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)#Blog 모델명
    return render(request, 'detail.html', {'blog_detail':blog_detail})

def write(request):
    return render(request, 'write.html')

def send(request):
    if(request.method == 'POST'):
        blog = Blog()
        blog.title = request.POST['title']
        blog.body = request.POST['body']
        blog.pub_date = timezone.datetime.now()
        blog.description = request.POST['description']
        blog.save()
        for img in request.FILES.getlist('image'):
            photo = Photo()
            photo.post = blog
            photo.image = img
            photo.save()
        return redirect('/blog/' + str(blog.id))
    else:
        return render(request, 'new.html')

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