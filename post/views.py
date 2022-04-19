from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from post.models import MyPost
from django.views import generic
# Create your views here.

def index(request):
    posts = MyPost.objects.all()
    return render(request, 'post/homePage.html', {'posts': posts})

class PostDetailView(generic.DetailView):
    model = MyPost
    template_name = "post/post_detail.html"
    
def postAdd(request, pk):
    post = MyPost.objects.get(pk=pk)
    post.comments.add(comment=request.POST['comment'],user=request.user.account)
    return HttpResponseRedirect(reverse("post:post_detail",kwargs={"pk":pk}))
    