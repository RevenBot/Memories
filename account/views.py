
from django.http import HttpResponseRedirect
from django.shortcuts import  render, redirect
from django.views.generic import *
from django.contrib.auth.forms import UserCreationForm
from django.urls import *
from account.forms import NewAccountForm
from account.models import Account
from django.contrib.auth import views as auth_views
# Create your views here.


def index(request):
    return render(request, 'account/index.html')


class UserCreationForm(CreateView):
    form_class= UserCreationForm
    template_name="account/user_create.html"
    success_url=reverse_lazy("account:registrationAccount")
    

class userLogIn(auth_views.LoginView):
    
    template_name="registration/login.html"
    def form_valid(self, form):
        super().form_valid(form)
        user=self.request.user
        try:
            user.account
        except:
            return redirect('account:registrationAccount')
        else:
            return HttpResponseRedirect(self.get_success_url())
       
#FIXME: solo con metodo post? 
class AccountCreationForm(FormView):
    template_name="account/account_create.html"
    form_class= NewAccountForm
    success_url=reverse_lazy("index")
    def form_valid(self,form):
        #chiamato quando e' stato compilato correttamente il form
        Account.objects.create(user=self.request.user,firstname=form.cleaned_data['firstname_form'],surname=form.cleaned_data['surname_form'],information=form.cleaned_data['information_form'])
        return super().form_valid(form)

class AccountUpdateView(UpdateView):
    model = Account
    template_name = "account/account_update.html"
    #field i campi che devo mostrare (di question)
    fields=["firstname","surname","information"]
    success_url=reverse_lazy("account:index")
#TODO Delete e eliminare user