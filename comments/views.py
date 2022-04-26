from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from comments.models import Comments
from post.models import MyPost
from django.views.decorators.http import require_http_methods
# Create your views here.
@login_required
def commentAdd(request, pk):
    post = MyPost.objects.get(pk=pk)
    post.comments.create(comment=request.POST['comment'],user=request.user.account)
    return HttpResponseRedirect(reverse("post:post_detail",kwargs={"pk":pk}))
@login_required
@require_http_methods(["POST"])
def commentDelete(request, pk):
    postPK=request.POST['postPK']
    #user che vede il tasto cioe chi lo possiede e il autore del post
    userRequest=request.user.account
    # {% if user.account == comment.user or object in user.account.posts.all %}
    if userRequest==Comments.objects.get(pk=pk).user or  MyPost.objects.get(pk=postPK) in userRequest.posts.all():
        Comments.objects.get(pk=pk).delete()
    return HttpResponseRedirect(reverse("post:post_detail",kwargs={"pk":postPK}))