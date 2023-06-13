# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect 
from home.models import Post, AllComment ,Gellery, Members, AboutUs
from django.template import RequestContext
from datetime import datetime 
from django.utils.translation import gettext as _ 
from .forms import ContactForm, CommentForm, CreateUserForm
from django.contrib.auth.forms import UserCreationForm 
from django.contrib import messages
from django.contrib.auth.models import Group 
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required 
from .decorators import unauthenticated_user, allowed_users, admin_only
from .models import Viewer
from .forms import ViewerForm, GellaryForm, PostForm, MembersForm, AboutUsForm


# Create your views here.
# def index(request):
#     post_dic = { 'posts' : 'hello world'}
#     return render(request, 'home/index.html',context=post_dic)

def errorhandler(request,exception):
    return render(request, 'not-found.html')


def index(request):
    campus = Post.objects.filter(category='ক্যাম্পাস')
    hall = Post.objects.filter(category='হল')
    club = Post.objects.filter(category='ক্লাব')
    sports = Post.objects.filter(category='স্পোর্টস')
    alumni = Post.objects.filter(category='এলামনাই')
    blog = Post.objects.filter(category='ব্লগ') 
    all_posts = Post.objects.order_by('date').reverse()
    images = Gellery.objects.order_by('date').reverse()
    post_dic = { 'campuses' : campus[::-1], 'halls': hall[::-1], 'clubs': club[::-1], 'sports': sports[::-1], 'alumnies': alumni[::-1], 'blogs': blog[::-1], 'posts' : all_posts, 'images':images }
    return render(request, 'home/index.html',context=post_dic)

def campus(request):
    campus = Post.objects.filter(category='ক্যাম্পাস')
    hall = Post.objects.filter(category='হল')
    club = Post.objects.filter(category='ক্লাব')
    sports = Post.objects.filter(category='স্পোর্টস')
    alumni = Post.objects.filter(category='এলামনাই')
    blog = Post.objects.filter(category='ব্লগ') 
    all_posts = Post.objects.order_by('date').reverse()
    post_dic = { 'campuses' : campus[::-1], 'halls': hall[::-1], 'clubs': club[::-1], 'sports': sports[::-1], 'alumnies': alumni[::-1], 'blogs': blog[::-1], 'posts' : all_posts }
    return render(request, 'home/campus.html',context=post_dic)

def hall(request):
    campus = Post.objects.filter(category='ক্যাম্পাস')
    hall = Post.objects.filter(category='হল')
    club = Post.objects.filter(category='ক্লাব')
    sports = Post.objects.filter(category='স্পোর্টস')
    alumni = Post.objects.filter(category='এলামনাই')
    blog = Post.objects.filter(category='ব্লগ') 
    all_posts = Post.objects.order_by('date').reverse()
    post_dic = { 'campuses' : campus[::-1], 'halls': hall[::-1], 'clubs': club[::-1], 'sports': sports[::-1], 'alumnies': alumni[::-1], 'blogs': blog[::-1], 'posts' : all_posts }
    return render(request, 'home/hall.html',context=post_dic)

def club(request):
    campus = Post.objects.filter(category='ক্যাম্পাস')
    hall = Post.objects.filter(category='হল')
    club = Post.objects.filter(category='ক্লাব')
    sports = Post.objects.filter(category='স্পোর্টস')
    alumni = Post.objects.filter(category='এলামনাই')
    blog = Post.objects.filter(category='ব্লগ') 
    all_posts = Post.objects.order_by('date').reverse()
    post_dic = { 'campuses' : campus[::-1], 'halls': hall[::-1], 'clubs': club[::-1], 'sports': sports[::-1], 'alumnies': alumni[::-1], 'blogs': blog[::-1], 'posts' : all_posts }
    return render(request, 'home/club.html',context=post_dic)

def sports(request):
    campus = Post.objects.filter(category='ক্যাম্পাস')
    hall = Post.objects.filter(category='হল')
    club = Post.objects.filter(category='ক্লাব')
    sports = Post.objects.filter(category='স্পোর্টস')
    alumni = Post.objects.filter(category='এলামনাই')
    blog = Post.objects.filter(category='ব্লগ') 
    all_posts = Post.objects.order_by('date').reverse()
    post_dic = { 'campuses' : campus[::-1], 'halls': hall[::-1], 'clubs': club[::-1], 'sports': sports[::-1], 'alumnies': alumni[::-1], 'blogs': blog[::-1], 'posts' : all_posts }
    return render(request, 'home/sports.html',context=post_dic)

def alumni(request):
    campus = Post.objects.filter(category='ক্যাম্পাস')
    hall = Post.objects.filter(category='হল')
    club = Post.objects.filter(category='ক্লাব')
    sports = Post.objects.filter(category='স্পোর্টস')
    alumni = Post.objects.filter(category='এলামনাই')
    blog = Post.objects.filter(category='ব্লগ') 
    all_posts = Post.objects.order_by('date').reverse()
    post_dic = { 'campuses' : campus[::-1], 'halls': hall[::-1], 'clubs': club[::-1], 'sports': sports[::-1], 'alumnies': alumni[::-1], 'blogs': blog[::-1], 'posts' : all_posts }
    return render(request, 'home/alumni.html',context=post_dic)

def blog(request):
    campus = Post.objects.filter(category='ক্যাম্পাস')
    hall = Post.objects.filter(category='হল')
    club = Post.objects.filter(category='ক্লাব')
    sports = Post.objects.filter(category='স্পোর্টস')
    alumni = Post.objects.filter(category='এলামনাই')
    blog = Post.objects.filter(category='ব্লগ') 
    all_posts = Post.objects.order_by('date').reverse()
    post_dic = { 'campuses' : campus[::-1], 'halls': hall[::-1], 'clubs': club[::-1], 'sports': sports[::-1], 'alumnies': alumni[::-1], 'blogs': blog[::-1], 'posts' : all_posts }
    return render(request, 'home/blog.html',context=post_dic)

def gellery(request):
    campus = Post.objects.filter(category='ক্যাম্পাস')
    hall = Post.objects.filter(category='হল')
    club = Post.objects.filter(category='ক্লাব')
    sports = Post.objects.filter(category='স্পোর্টস')
    alumni = Post.objects.filter(category='এলামনাই')
    blog = Post.objects.filter(category='ব্লগ') 
    all_posts = Post.objects.order_by('date').reverse()
    images = Gellery.objects.order_by('date').reverse()
    post_dic = { 'campuses' : campus[::-1], 'halls': hall[::-1], 'clubs': club[::-1], 'sports': sports[::-1], 'alumnies': alumni[::-1], 'blogs': blog[::-1], 'posts' : all_posts , 'images':images}
    return render(request,'home/gellery.html',context=post_dic)

def about(request):
    campus = Post.objects.filter(category='ক্যাম্পাস')
    hall = Post.objects.filter(category='হল')
    club = Post.objects.filter(category='ক্লাব')
    sports = Post.objects.filter(category='স্পোর্টস')
    alumni = Post.objects.filter(category='এলামনাই')
    blog = Post.objects.filter(category='ব্লগ') 
    all_posts = Post.objects.order_by('date').reverse()
    members = Members.objects.order_by('id')
    aboutus = AboutUs.objects.order_by('id')
    post_dic = { 'campuses' : campus[::-1], 'halls': hall[::-1], 'clubs': club[::-1], 'sports': sports[::-1], 'alumnies': alumni[::-1], 'blogs': blog[::-1], 'posts' : all_posts , 'members':members, 'aboutus':aboutus}
    return render(request,'home/about.html',context=post_dic)


def post(request,id):
    try:
        comment_form = CommentForm()
        post = Post.objects.get(id=id)
        all_posts = Post.objects.order_by('date').reverse()
        # context = {'post': post, 'posts' : all_posts,'form': form}

        if request.method == "POST":
            comment_form = CommentForm(request.POST)

            if comment_form.is_valid():
                instance = comment_form.save(commit=False)
                instance.post = post
                instance.user = request.user
                instance.save() 
                context = {'post': post, 'posts' : all_posts,'form': comment_form}
                return render(request, 'home/viewpost.html', context)
            else:
                return HttpResponseRedirect('/something wrong/')  

        context = {'post': post, 'posts' : all_posts,'form': comment_form}
        return render(request, 'home/viewpost.html', context)
       
        # return render(request, 'home/viewpost.html', context)

    except Post.DoesNotExist:
        return render(request, 'not-found.html')




def contact(request): 
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST) 

        if form.is_valid():
            form.save()
            return render(request,'home/success.html') 
        else:
            return render(request,'home/failed.html') 

    return render(request, 'home/contact.html',{'form':form})


@unauthenticated_user
def signup(request):
    form = CreateUserForm()

    if(request.method == "POST"):
        form = CreateUserForm(request.POST)
        print(form) 
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            # group = Group.objects.get(name="customers")
            # user.groups.add(group)

            # Customer.objects.create(user = user, name = user.username)

            messages.success(request,"Accout was created successfully for " + username )
            return redirect('signin')

        else:
            print(messages)

    context = {'form':form}
    return render(request, 'home/signup.html',context)

@unauthenticated_user
def signin(request):
    
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request,username = username, password = password)

        if user is not None:
            login(request,user)
            return redirect("/")
        else:
            messages.info(request,"username or password is incorrect")
                
    context = {}
    return render(request, 'home/signin.html', context)

def logoutUser(request):
    logout(request)
    return redirect("signin")


@login_required(login_url='signin')
@allowed_users(allowed_roles=['viewer','admin'])
def profile(request):
    viewer = request.user.viewer
    context = {'viewer': viewer}
    print(request.user.viewer)
    return render(request,'home/profile.html',context) 


@allowed_users(allowed_roles=['viewer','admin'])
def accountSettings(request):
    user = request.user.viewer  
    form = ViewerForm(instance=user)
    print(user)
    if request.method == "POST":
        form = ViewerForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')

    context = {'form' : form ,'user': user}
    return render(request,'home/edit.html',context)

@admin_only
def editImage(request,id):
    image = Gellery.objects.get(id=id) 
    form = GellaryForm(instance=image)

    if request.method == "POST":
        form = GellaryForm(request.POST, request.FILES, instance=image)
        if form.is_valid():
            form.save()
            print("msg : ",messages)
            return redirect('dashboard')
        else:
            print(messages)

    context = {'form' : form ,'image': image}
    return render(request,'home/edit_image.html',context)

@admin_only
def editAbout(request):
    about = AboutUs.objects.get(id=1) 
    form = AboutUsForm(instance=about)

    if request.method == "POST":
        form = AboutUsForm(request.POST, request.FILES, instance=about)
        if form.is_valid():
            form.save()
            print("msg : ",messages)
            return redirect('dashboard')
        else:
            print(messages)

    context = {'form' : form ,'about': about}
    return render(request,'home/edit_about.html',context)

@admin_only
def editMember(request,id):
    member = Members.objects.get(id=id) 
    form = MembersForm(instance=member)

    if request.method == "POST":
        form = MembersForm(request.POST, request.FILES, instance=member)
        if form.is_valid():
            form.save()
            print("msg : ",messages)
            return redirect('dashboard')
        else:
            print(messages)

    context = {'form' : form ,'member': member}
    return render(request,'home/edit_member.html',context)


@admin_only
def editPost(request,id):
    post = Post.objects.get(id=id) 
    form = PostForm(instance=post)

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        else:
            print(form)

    context = {'form' : form ,'post': post}
    return render(request,'home/edit_post.html',context)

@admin_only
def deleteImage(request,id):
    image = Gellery.objects.get(id=id)
    image.delete()
    return redirect('dashboard')

@admin_only
def deleteMembers(request,id):
    member = Members.objects.get(id=id)
    member.delete()
    return redirect('dashboard')


@admin_only
def deletePost(request,id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect('dashboard')

@admin_only
def addImage(request): 
    form = GellaryForm(request.POST, request.FILES)

    if request.method == 'POST':
        form = GellaryForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('dashboard') 
        else:
            print(form)

    return render(request, 'home/addImage.html',{'form':form})

@admin_only
def addMember(request): 
    form = MembersForm(request.POST, request.FILES)

    if request.method == 'POST':
        form = MembersForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('dashboard') 
        else:
            print(form)

    return render(request, 'home/addMember.html',{'form':form})

@admin_only
def addPost(request): 
    form = PostForm(request.POST, request.FILES)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('dashboard') 
        else:
            print(form)

    return render(request, 'home/addPost.html',{'form':form})


@login_required(login_url='signin')
@admin_only
def dashboard(request):
    campus = Post.objects.filter(category='ক্যাম্পাস')
    hall = Post.objects.filter(category='হল')
    club = Post.objects.filter(category='ক্লাব')
    sports = Post.objects.filter(category='স্পোর্টস')
    alumni = Post.objects.filter(category='এলামনাই')
    blog = Post.objects.filter(category='ব্লগ') 
    all_posts = Post.objects.order_by('date').reverse()
    images = Gellery.objects.order_by('date').reverse()
    members = Members.objects.order_by('id')
    viewers = Viewer.objects.all()
    total_posts = all_posts.count()
    total_viewers = viewers.count()

    context = { 'campuses' : campus[::-1], 'halls': hall[::-1], 'clubs': club[::-1], 'sports': sports[::-1], 'alumnies': alumni[::-1], 'blogs': blog[::-1], 'posts' : all_posts, 'images':images, 'members':members,"viewers":viewers,"total_posts":total_posts, "total_viewers":total_viewers }

    return render(request,'home/dashboard.html',context)
