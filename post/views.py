
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.http import Http404, HttpResponseRedirect
from post.models import MyPost
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_http_methods

# Create your views here.

def index(request):
    posts = MyPost.objects.all()
    return render(request, 'post/homePage.html', {'posts': posts})

class PostDetailView(generic.DetailView):
    model = MyPost
    template_name = "post/postDetail.html"
@method_decorator(login_required, name='dispatch')
class PostCreateView(generic.CreateView):
    model = MyPost
    template_name = "polls/question_create.html"
    fields=["name","description","image","categories"]
    template_name = "post/createPost.html"
    success_url=reverse_lazy("index")
    def get_success_url(self):
        pk = self.object.id
        return reverse("post:post_detail", kwargs={"pk": pk})
    def form_valid(self, form):
        super().form_valid(form)
        print(self.object)
        self.request.user.account.posts.add(self.object)
        return super().form_valid(form)
@login_required
#FIXME
def deleteView(request,pk):
    post=MyPost.objects.get(pk=pk)
    if request.user.account.posts.filter(pk=post.id).exists():
        post.delete()
    return HttpResponseRedirect(reverse("index"))
@method_decorator(login_required, name='dispatch')
# @method_decorator(require_http_methods(["POST"]), name='dispatch')
class editView(generic.UpdateView):
    model = MyPost
    template_name = "post/post_edit.html"
    fields=["name","description","image","categories"]# scegliere i commenti da mostrare
    # def get_initial(self):
    #     initial = super().get_initial()
    #     print(self.object)
    #     return initial
    def get_object(self):
        post=MyPost.objects.get(pk=self.kwargs["pk"])
        try:
            return self.request.user.account.posts.get(pk=post.id)
        except MyPost.DoesNotExist:
            self.success_url=reverse("index")
            raise Http404("Non puoi modificare quello che non e' tuo.")
        
    def get_success_url(self):
       pk = self.kwargs["pk"]
       return reverse("post:post_detail", kwargs={"pk": pk})