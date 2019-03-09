
from django import forms

class OrderForm(forms.Form):


        name = forms.CharField(required=True, label='Nimi', widget=forms.TextInput(attrs={'class': 'form-control'}))
        message = forms.CharField(required=True,widget=forms.Textarea(attrs={'class': 'form-control'}), label='Viesti')    
        email = forms.EmailField(required=True, label='Sähköposti', widget=forms.TextInput(attrs={'class': 'form-control'}))
        phone = forms.CharField(required=False, label='Puhelinnumero', widget=forms.TextInput(attrs={'class': 'form-control'}))
        place = forms.CharField(required=False, label='Tapahtumapaikka', widget=forms.TextInput(attrs={'class': 'form-control'}))
        #amount = forms.IntegerField(required=True, label='Vierasmäärä', widget=forms.NumberInput(attrs={'class': 'form-control'}))
