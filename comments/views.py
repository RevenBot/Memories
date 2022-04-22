from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from post.models import MyPost
# Create your views here.
#FIXME only user logged
def commentAdd(request, pk):
    post = MyPost.objects.get(pk=pk)
    post.comments.create(comment=request.POST['comment'],user=request.user.account)
    return HttpResponseRedirect(reverse("post:post_detail",kwargs={"pk":pk}))
    #TODO delete e update