from django.shortcuts import render
from  blog.forms import CommentForm
from django.http import HttpResponseRedirect
# Create your views here.

from django.shortcuts import render
from blog.models import Post, Comment

def blog_index(request):
    print("hi index1")
    posts = Post.objects.all().order_by('-created_on')
    context = {
        "posts": posts,
    }
    print(context.values())
    return render(request, "blog_index.html", context)

def blog_category(request, category):#input:str
    print("hi category1")
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by(
        '-created_on'
    )
    print(posts.values())
    context = {
        "category": category,
        "posts": posts
    }
    print(context.values())
    return render(request, "blog_category.html", context)

def blog_detail(request, pk):#input :int
    #single page no change url :get request or post request
    print('hi')
    post = Post.objects.get(pk=pk)
    print(post)
    form = CommentForm()
    print(form)
    print("hi2")
    if request.method == 'POST':
        print("hi3")
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post
            )
            comment.save()
    print('hi4')
    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form": form,
    }
    print(context.values())
    return render(request, "blog_detail.html", context)
def binance_index(request):
        return HttpResponseRedirect("https://knowledgecomputer2018.github.io/index2.html")
