from django.shortcuts import render, redirect
from Blog.models import  Profile, Post
from .forms import ProfileImage
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='/login/')
def profile(request):
    profile =  Profile.objects.get(username = request.user.username)
    article_written = Post.objects.filter(authour = request.user).order_by('-created')
    context = {
        'profile': profile,
        'article_written':article_written
    }
    return render(request, 'userprofile/profile.html', context)

@login_required(login_url='/login/')
def setting(request):
    change = Profile.objects.get(username = request.user.username)

    if request.method  == 'POST':
        form = ProfileImage(request.POST, request.FILES, instance=change)

        # user
        change.firstname = request.POST['firstname']
        change.email = request.POST['email']
        if form.is_valid():
            form.save()
        # basic
        change.website = request.POST['website']
        change.location = request.POST['location']
        change.bio = request.POST['bio']
        change.tag = request.POST['tag']

        # coding
        change.learning = request.POST['learning']
        change.available = request.POST['available']
        change.skill = request.POST['skill']
        change.project = request.POST['project']

        # work
        change.work = request.POST['work']
        change.education = request.POST['education']
        change.save()
        return redirect ('/setting/')
    else:
        imageform = ProfileImage(instance = change)
        context = {
            'change': change,
            'profile_img': imageform
        }
    return render(request, 'userprofile/setting.html',context)

