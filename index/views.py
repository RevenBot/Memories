from django.shortcuts import render
from category.models import MyCategory
from post.models import MyPost
# Create your views here.



def index(request):
    categories = MyCategory.objects.all()
    posts= MyPost.objects.all()
    context = {'categories': categories, 'posts': posts}
    return render(request, 'index/homePage.html',context)