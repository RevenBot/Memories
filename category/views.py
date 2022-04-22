from django.shortcuts import render
from django.views import generic

from .models import MyCategory
# Create your views here.
def index(request):
    categories = MyCategory.objects.all()
    context = {'categories': categories}
    return render(request, 'category/homePage.html',context)
class CategoryDetailView(generic.DetailView):
    model=MyCategory
    templateName='category/mycategory_detail.html'
    #TODO passare anche i post con quella categoria
    #TODO create solo da admin