from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from account.models import Account





class NewAccountForm(forms.Form):
    firstname_form = forms.CharField(max_length=100,required=True)
    surname_form = forms.CharField(max_length=100,required=True)
    information_form = forms.CharField(max_length=100,required=True)
    
 