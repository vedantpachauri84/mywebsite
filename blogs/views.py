from datetime import datetime
from django.shortcuts import render
from django.http import Http404,HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
from django.http import HttpResponseNotFound
from .models import Post, Ideas
from.forms import CommentForm
from.forms import PostForm
# Dictionary of blogs
def index(request):
    return render(request, 'blogs/blank.html')

# Home Page
def home(request):
    list2 = Post.objects.all().order_by("title")
    return render(request, 'blogs/index.html', {"list3": list2})

# Show all blogs
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

def about(request, blogname):

    blog = get_object_or_404(Post, title=blogname)
    comments = blog.comments.all()
    ideas=Ideas.objects.all()

    if request.method == "POST":
        form = CommentForm(request.POST)
        ideas=Ideas(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = blog
            comment.save()
            ideas=ideas.save(commit=False)
            ideas.post = blog
            ideas.save()

            return HttpResponseRedirect(
                reverse('about', args=[blogname])
            )
    else:
        form = CommentForm()
        ideas=Ideas.objects.all()

    return render(request, 'blogs/about.html', {
        "blog": blog,
        "comments": comments,
        "form": form,
        "ideas": ideas,
    })

