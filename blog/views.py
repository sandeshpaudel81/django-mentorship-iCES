from django.shortcuts import render, redirect
from .models import BlogPost
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login')
def home(request):
    allPosts = BlogPost.objects.all()
    context = {'posts': allPosts}
    return render(request, "home.html", context=context)


def blogDetail(request, id):
    singlePost = BlogPost.objects.get(id=id)
    context = {'post': singlePost}
    return render(request, 'blog-detail.html', context=context)


def addBlog(request):
    if request.method == "POST":
        post_title = request.POST['title']
        post_slug = request.POST['slug']
        post_content = request.POST['content']
        BlogPost.objects.create(title=post_title, content=post_content, slug=post_slug)
        return redirect('/add/')
    return render(request, 'add-blog.html')


def editBlog(request, id):
    if request.method == "POST":
        post_title = request.POST['title']
        post_slug = request.POST['slug']
        post_content = request.POST['content']
        post = BlogPost.objects.get(id=id)
        post.title = post_title
        post.slug = post_slug
        post.content = post_content
        post.save()
        return redirect('/blog/'+str(id))
    post = BlogPost.objects.get(id=id)
    context = {'post':post}
    return render(request, 'edit-blog.html', context=context)


def deleteBlog(request, id):
    post = BlogPost.objects.get(id=id)
    post.delete()
    return redirect('/')


def loginUser(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm()
    context = {'form':form}
    return render(request, 'login.html', context=context)


def registerUser(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('/login')
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'register.html', context=context)


def logoutUser(request):
    logout(request)
    return redirect('/login')