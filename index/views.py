from django.shortcuts import render
from category.models import MyCategory
from post.models import MyPost
from django.core.paginator import Paginator
# Create your views here.


def welcome(request):
    return render(request, 'index/welcome.html')

def testIndex(request):
    categories = MyCategory.objects.all()
    posts= MyPost.objects.all()
    context = {'categories': categories, 'posts': posts}
    return render(request, 'index/accountInfo.html',context)

def index(request):
    categories = MyCategory.objects.all()
    posts= Paginator(MyPost.objects.all().order_by('-created_at'),4)
    recentPosts = MyPost.objects.all().order_by('-created_at')[:5]
    page_number = request.GET.get('page')
    page_posts = posts.get_page(page_number)
    context = {'categories': categories, 'page_posts': page_posts, 'recentPosts': recentPosts}
    return render(request, 'index/index.html',context)

def test(request):
    posts= MyPost.objects.all()
    context = {'page_posts': posts}
    return render(request, 'index/account.html',context)