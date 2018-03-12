
from django import forms

class OrderForm(forms.Form):

        fields = ('Etunimi', 'Sukunimi', 'Sähköposti', 'Puhelinnumero','Tapahtuma', 'Tapahtumapaikka','Määrä','Viesti',)
        name = forms.CharField(required=True, label='Nimi')
        email = forms.EmailField(required=True, label='Sähköposti')
        phone = forms.CharField(required=False, label='Puhelinnumero')
        place = forms.CharField(required=False, label='Tapahtumapaikka')
        amount = forms.IntegerField(required=True, label='Vierasmäärä')
        message = forms.CharField(required=True,widget=forms.Textarea, label='Viesti')
        #widgets = {
        #    'Etunimi': forms.TextInput(attrs={'class': 'form-control','id':'Etunimi', 'required': True, 'name': 'Etunimi',}),
        #    'Sukunimi': forms.TextInput(attrs={'class': 'form-control', 'id':'Sukunimi', 'required': True,}),
        #    'Sähköposti': forms.TextInput(attrs={'class': 'form-control', 'id': 'Sähköposti', 'required': True,}),
        #    'Puhelinnumero': forms.TextInput(attrs={'class': 'form-control', 'id': 'Puhelinnumero',}),
        #    'Tapahtuma': forms.TextInput(attrs={'class': 'form-control', 'id': 'Tapahtuma', 'required': True,}),
        #    'Päivänmäärä': forms.DateInput(attrs={'class': 'form-control', 'id': 'Päivänmäärä', 'required': True,}),
        #    'Tapahtumapaikka': forms.TextInput(attrs={'class': 'form-control', 'id': 'Tapahtumapaikka',}),
            #'Päivänmäärä': forms.NumberInput(attrs={'class': 'form-control', 'id': 'Määrä', 'required': True,}),
        #    'Viesti': forms.TextInput(attrs={'class': 'form-control', 'id': 'Viesti', 'required': True,}),
        #}
