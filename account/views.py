
from django.shortcuts import render
from django.views.generic import *
from django.urls import *
from account.forms import NewAccountForm
from account.models import Account
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login
from django.views.decorators.http import require_http_methods
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator
# Create your views here.


def index(request):
    return render(request, 'account/index.html')

@method_decorator(require_http_methods(["POST","GET"]), name='dispatch')
class UserCreationForm(FormView):
    form_class= NewAccountForm
    template_name="account/user_create.html"
    success_url=reverse_lazy("index")
    def form_valid(self,form):
        form.save()
        user=authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
        login(self.request, user)
        my_group = Group.objects.get(name='Utenti') 
        my_group.user_set.add(user)
        Account.objects.create(user=user,firstname=form.cleaned_data['nome'],surname=form.cleaned_data['cognome'],information=form.cleaned_data['informazioni'],email=form.cleaned_data['email'],mobile=form.cleaned_data['numero_di_telefono'],address=form.cleaned_data['indirizzo'],country=form.cleaned_data['stato'],date_of_birth=form.cleaned_data['data_di_nascita'])
        return super().form_valid(form)
       


@method_decorator(require_http_methods(["POST","GET"]), name='dispatch')
class AccountUpdateView(UpdateView):
    model = Account
    template_name = "account/account_update.html"
    #field i campi che devo mostrare (di question)
    fields=['information','email','mobile','address','country']
    
    def get_object(self):
        return self.request.user.account
    def get_success_url(self):
       pk = self.kwargs["pk"]
       return reverse("account:profile", kwargs={"pk": pk})


@method_decorator(require_http_methods(["POST","GET"]), name='dispatch')
class AccountDeleteView(DeleteView):
    model = Account
    template_name = "account/account_delete.html"
    success_url=reverse_lazy("index")
    def get_object(self):
        return self.request.user.account
    def form_valid(self,form):
        user=self.request.user
        user.delete()
        return super().form_valid(form)
    
    
@require_http_methods(["POST","GET"])
def profile(request,pk):
    account=request.user.account
    posts= Paginator(account.posts.all(),4)
    page_number = request.GET.get('page')
    page_posts = posts.get_page(page_number)
    context={'account':account,'page_posts':page_posts}
    return render(request, 'account/profile.html',context)