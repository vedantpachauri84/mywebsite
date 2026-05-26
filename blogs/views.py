from datetime import datetime
from django.shortcuts import render
from django.http import Http404,HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
from django.http import HttpResponseNotFound
from .models import Post, Ideas
from.forms import CommentForm
from.forms import PostForm
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


def register(request):

    if request.method == 'POST':
        username =request.POST.get('username')
        email=request.POST.get('email')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        if password1 == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already registered')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already registered')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Passwords do not match')

            return render(request, 'blogs/allposts.html')
    else:
        return render(request, 'blogs/includes/register.html')
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        user = auth.authenticate(username=username, password=password1)
        if user is not None:
            auth.login(request=request, user=user)
            return redirect('home')

        else:
            messages.info(request, 'Username or password is incorrect')
            return redirect('login')
    else:
             return render(request, 'blogs/includes/login.html')
def logout(request):
    auth.logout(request)
    return redirect('login')

@login_required(login_url='login')
def index(request):
    return render(request, 'blogs/blank.html')

@login_required(login_url='login')
def home(request):
    list2 = Post.objects.all().order_by("title")
    return render(request, 'blogs/index.html', {"list3": list2})

@login_required(login_url='login')
def allposts(request):
    list2=Post.objects.all()
    return render(request, 'blogs/allposts.html', {"list3": list2})


# Individual blog page
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Post
from .forms import CommentForm

from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
@login_required(login_url='login')
def about(request, blogname):

    blog = get_object_or_404(Post, title=blogname)
    comments = blog.comments.all()

    if request.method == "POST":
        form = CommentForm(request.POST)


        if form.is_valid() :

            comment = form.save(commit=False)
            comment.post = blog
            comment.save()



            return HttpResponseRedirect(
                reverse('about', args=[blogname])
            )

    else:
        form = CommentForm()


    return render(request, 'blogs/about.html', {
        "blog": blog,
        "comments": comments,
        "form": form,

    })