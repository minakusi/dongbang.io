from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.utils import timezone
# Create your views here.
from .models import Blog

def home(request):
    blog_list = Blog.objects.get_queryset().order_by('id')
    sliced = Paginator(blog_list,3)
    page_num = request.GET.get('page')
    send_this = sliced.get_page(page_num)

    return render(request, 'home.html', {'posts' : send_this})

def detail(request, abc):
    blog_detail = get_object_or_404(Blog, pk=abc)
    return render(request, 'detail.html', {'a' : blog_detail})

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/'+str(blog.id))

def new(request):
    return render(request,'new.html')

