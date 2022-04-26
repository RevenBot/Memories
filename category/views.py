from unicodedata import name
from django.shortcuts import render
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from post.models import MyPost
from django.contrib.auth.decorators import permission_required
from .models import MyCategory
from django.views import generic
from django.utils.decorators import method_decorator
# Create your views here.
def categoryDetailView(request,pk):
    category = MyCategory.objects.get(pk=pk)
    posts = Paginator(MyPost.objects.filter(categories=category).order_by('-created_at'),6)
    page_number = request.GET.get('page')
    page_posts = posts.get_page(page_number)
    context = {'category': category, 'page_posts': page_posts}
    return render(request, 'category/mycategory_detail.html',context)


@method_decorator(permission_required('category.view_category', login_url='/admin/'),name='dispatch')
class CategoryCreateView(generic.CreateView):
    model = MyCategory
    template_name = "category/category_create.html"
    fields=["name","description","image"]
    success_url=reverse_lazy("index")