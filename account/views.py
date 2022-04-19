
from django.shortcuts import  render
from django.views.generic import *
from django.contrib.auth.forms import UserCreationForm
from django.urls import *
from account.forms import NewAccountForm
from account.models import Account
# Create your views here.


def index(request):
    return render(request, 'account/index.html')


class UserCreationForm(CreateView):
    form_class= UserCreationForm
    template_name="account/user_create.html"
    success_url=reverse_lazy("account:registrationAccount")
#FIXME: solo con post? 
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