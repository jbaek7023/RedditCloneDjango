from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from . import models
from django.contrib.auth.models import User

# Create your views here.
@login_required
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['url']:
            post = models.Post()
            post.title = request.POST['title']
            post.url = request.POST['url']
            post.pub_date = timezone.datetime.now()
            post.author = request.user

            post.save()
            return redirect('home')
        else:
            return render(request, 'posts/create.html', {'error': 'Fill the form!'})
    else:
        return render(request, 'posts/create.html')

def home(request):
    posts = models.Post.objects.order_by('votes_total')
    return render(request, 'posts/index.html', {'posts': posts})

def home_user(request, fk):
    # posts = models.Post.objects.get(author=user_name).order_by('votes_total')
    posts = models.Post.objects.filter(author=fk).order_by('votes_total')
    author = User.objects.get(pk=fk)
    return render(request, 'posts/user_by.html', {'posts': posts, 'user_name':author})

def upvote(request, pk):
    if request.method == 'POST':
        post = models.Post.objects.get(pk = pk)
        post.votes_total  = post.votes_total + 1
        post.save()
        return redirect('home')

def downvote(request, pk):
    if request.method == 'POST':
        post = models.Post.objects.get(pk = pk)
        post.votes_total  = post.votes_total - 1  
        post.save()
        return redirect('home')