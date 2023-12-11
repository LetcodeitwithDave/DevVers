from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.http import HttpResponseRedirect
from  django.contrib import messages
from django.contrib.auth import authenticate , login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, ImageForm
from .models import Profile, Post


# Create your views here.
@login_required(login_url='/login/')
def home(request):
    post = Post.objects.order_by('-created')
    profile =  Profile.objects.get(username = request.user.username)
 
    context =  {
        'post':post,
        'tag' : profile
    }
    
    return render(request, "Blog/home.html", context)

def register(request):
    if request.user.is_authenticated:
        return redirect('/home/')
    elif request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid(): 
            form.save()
            username = form.cleaned_data['username']
            firstname = form.cleaned_data['first_name']
            email =  form.cleaned_data['email']
            # password = form.cleaned_data['password1']
            Profile.objects.create(username=username, firstname=firstname, email=email)
            Post.objects.create(authour=username, content = "", title = "")

            messages.success(request, f'Account created successfully for {username}.')
            
            return redirect('/login/')   
    else:
        form = RegisterForm()
    return render(request, "Blog/register.html", {'form':form} )

def loginpage(request):
    if request.user.is_authenticated:
        return redirect('/home/')
    
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # authenticate user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/home/')
        else: 
            messages.warning(request, 'Either username or password is incorrect!')    
    return render(request, "Blog/login.html")


def about(request):
    return render(request, 'Blog/about.html', {'title':'about'})    


@login_required(login_url='/login/')
def logoutpage(request):
    logout(request)
    messages.success(request, 'Logout successful.')
    return redirect('/login/')

    



def readpost(request, post_id):
    post = Post.objects.get(id= post_id)
    username = request.user.username
    context = {
        'post': post,
        'username': username,   
    }
    return render(request,'Blog/readpost.html', context )   

def edit(request, edit_id):
    editpost = Post.objects.get(id = edit_id)

    if request.method == 'POST':
        form = ImageForm( request.POST, request.FILES, instance=editpost)
        if form.is_valid():
            form.save()
        editpost.title = request.POST['title']
        editpost.content = request.POST['content']
        editpost.save()
        return redirect ('/home/')
    else:
        data = ImageForm(instance=editpost)
        return render(request, 'Blog/edit.html',{'edit': editpost, 'data':data})

######
@login_required(login_url='/login/')
def post(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            title = request.POST['title']
            content = request.POST['content']
            picture = form.cleaned_data['post_img']
            if len(title )< 1:
                messages.warning(request, 'Post must have a title!')
                return redirect('/post/')
            elif len(content) <3:
                messages.warning(request, 'Content must contain more than 2 character.')
            else:
                Post.objects.create(title=title, content=content, post_img=picture)
                return redirect('/home/')
    else:
        form = ImageForm()
    return render(request, 'Blog/post.html', {'data': form, 'title': 'post'})

def search (request):
    if request.method == 'POST':
        search_value =  request.POST['search']
        search_result = Post.objects.filter(title__contains =search_value)
    context = {
        'value': search_value,
        'search_result': search_result
    }
    return render(request, 'Blog/search.html', context)

def delete_confirmation(request, id):
        try:
            post_id = Post.objects.get(id = id)
            context = {
                'post_id': post_id, 
            }
            # gonna rap this up later
        except Post.DoesNotExist :
            return HttpResponse(f'<h1> there is no data available </h1>')
        return render(request, 'Blog/delete_confirmation.html', context)


def delete(request, delete_id):
        data  = Post.objects.get(id = delete_id)
        data.delete()
        return redirect('/profile/')






        

