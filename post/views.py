from django.shortcuts import render
from .models import Post

# Create your views here.
def posts(request):
    blog_posts= Post.objects.all()  
    context = {
        "blog_posts" : blog_posts
    }  
    return render(request,'posts.html',context)
 
def postdetails(request,id):
    post = Post.objects.get(id = id)
    context = {
        "post" : post
    }
    return render(request,'postdetails.html',context)