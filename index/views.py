from django.shortcuts import render
from category.models import MyCategory
from post.models import MyPost
from django.core.paginator import Paginator
# Create your views here.


def welcome(request):
    return render(request, 'index/welcome.html')

def index(request):
    categories = MyCategory.objects.all()
    posts= MyPost.objects.all()
    
    context = {'categories': categories, 'posts': posts}
    return render(request, 'index/homePage.html',context)

def testIndex(request):
    categories = MyCategory.objects.all()
    posts= Paginator(MyPost.objects.all(),1)
    page_number = request.GET.get('page')
    page_posts = posts.get_page(page_number)
    context = {'categories': categories, 'page_posts': page_posts}
    return render(request, 'index/index.html',context)

def test(request):
    posts= MyPost.objects.all()[1]
    context = {'object': posts}
    return render(request, 'index/accountInfo.html',context)