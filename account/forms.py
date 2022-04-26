from datetime import date
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User
"""_summary_
Form per la creazione di un account(non ci sono Posts e User)
"""

class DateInput(forms.DateInput):
    input_type = 'date'

class NewAccountForm(UserCreationForm):
    nome = forms.CharField(max_length=100,required=True)
    cognome = forms.CharField(max_length=100,required=True)
    informazioni = forms.CharField(max_length=100,required=True)
    email = forms.CharField(max_length=100,required=True)
    numero_di_telefono = forms.CharField(max_length=100)
    indirizzo = forms.CharField(max_length=100)
    stato = forms.CharField(max_length=100,required=True)
    data_di_nascita = forms.DateTimeField(required=True,widget=DateInput())
    class Meta:
        model=User
        fields=('nome', 'cognome','informazioni','email','numero_di_telefono','indirizzo','stato','data_di_nascita','username','password1','password2')
        
        help_texts = {
            'username': "Inserisci un nome utente univoco, Lettere, numeri e @/./+/-/_ sono ammessi.",
        }
        widgets ={
            'data_di_nascita':DateInput(),
        }