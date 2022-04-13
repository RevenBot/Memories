from django.shortcuts import render
from django.views import generic

from .models import MyCategory
# Create your views here.
class CategoryDetailView(generic.DetailView):
    model=MyCategory
    templateName='category/mycategory_detail.html'