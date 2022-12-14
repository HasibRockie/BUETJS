# Create your views here.
from django.shortcuts import render
from home.models import Post 
from django.template import RequestContext
from datetime import datetime 
from django.utils.translation import gettext as _ 
from .forms import ContactForm, CommentForm 


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
    post_dic = { 'campuses' : campus[::-1], 'halls': hall[::-1], 'clubs': club[::-1], 'sports': sports[::-1], 'alumnies': alumni[::-1], 'blogs': blog[::-1], 'posts' : all_posts }
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

def post(request,id):
    try:
        form = CommentForm()
        post = Post.objects.get(id=id)
        all_posts = Post.objects.order_by('date').reverse()
        context = {'post': post, 'posts' : all_posts,'form': form}

        if request.method == "POST":
            form = CommentForm(request.POST)

            if form.is_valid():
                form.save()
                # return render(request, 'home/viewpost.html')

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

