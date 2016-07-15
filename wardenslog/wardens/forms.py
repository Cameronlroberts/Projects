from django.forms import ModelForm
from wardens.models import Incident
from django.contrib.auth.models import User
from django import forms


class IncidentForm(ModelForm):
    class Meta:
        model = Incident
        fields = '__all__'
        exclude = ['date_created', ]


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']