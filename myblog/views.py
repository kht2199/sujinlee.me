from django.shortcuts import render
from django.utils import timezone
from .models import Post, Project, Category
from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.template import RequestContext

def index(request):
    return render(request, 'blog/index.html')

def about(request):
    return render(request, 'blog/about.html')

def resume(request):
    return render(request, 'blog/resume.html')

#blog
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    post_id = post.pk
    liked = False
    try:
        next = post.get_next_by_published_date()
    except Post.DoesNotExist:
        next = None
    try:
        previous = post.get_previous_by_published_date()
    except Post.DoesNotExist:
        previous = None
    if request.session.get('has_liked_'+str(post_id), liked):
        liked = True
    context = {'post':post,'next':next,'previous':previous,"liked": liked}
    return render(request,'blog/post_detail.html', context)

# project
def project_list(request):
    projects = Project.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/project_list.html', {'projects':projects})

def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    project_id = project.pk
    liked = False
    try:
        next = project.get_next_by_published_date()
    except Project.DoesNotExist:
        next = None
    try:
        previous = project.get_previous_by_published_date()
    except Project.DoesNotExist:
        previous = None
    if request.session.get('has_liked_'+str(project_id), liked):
        liked = True
    context = {'project':project,'next':next,'previous':previous,"liked": liked}
    return render(request,'blog/project_detail.html', context)

#Likes
def like_count_blog(request):
    liked = False
    if request.method == 'GET':
        post_id = request.GET['post_id']
        post = Post.objects.get(id=int(post_id))
        if request.session.get('has_liked_'+post_id, False):
            print("unlike")
            if post.likes > 0:
                likes = post.likes - 1
                try:
                    del request.session['has_liked_'+post_id]
                except KeyError:
                    print("keyerror")
        else:
            print("like")
            request.session['has_liked_'+post_id] = True
            likes = post.likes + 1
    post.likes = likes
    post.save()
    return HttpResponse(likes, liked)

def like_count_project(request):
    liked = False
    if request.method == 'GET':
        project_id = request.GET['project_id']
        project = Project.objects.get(id=int(project_id))
        if request.session.get('has_liked_'+project_id, False):
            print("unlike")
            if project.likes > 0:
                likes = project.likes - 1
                try:
                    del request.session['has_liked_'+project_id]
                except KeyError:
                    print("keyerror")
        else:
            print("like")
            request.session['has_liked_'+project_id] = True
            likes = project.likes + 1
    project.likes = likes
    project.save()
    return HttpResponse(likes, liked)

def custom_404(request):
    return render_to_response('404.html')