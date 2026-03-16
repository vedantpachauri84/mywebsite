from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.template.loader import render_to_string

def home(request):
    return render(request, 'blogs/index.html')

    #res_data=render_to_string("blogs/index.html")
   #return HttpResponse(res_data)


blognames={
    "python":"this is python",
    "java":"this is java",
    "django":None,
}
def allposts(request):
    list2=list(blognames.keys())
    return render(request,'blogs/allposts.html',{"list3":list2})
def remove2(blogname):
    list=blogname.upper()
    return list

def about(request,blogname):
    try:
        blog=blognames[blogname]
        return render(request,'blogs/about.html',{"blogname":blogname,"blog":remove2(blogname)})
    except KeyError:
        return HttpResponseNotFound("Blogname not found")