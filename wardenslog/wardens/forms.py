from django.forms import ModelForm
from wardens.models import Incident
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,

)


class IncidentForm(ModelForm):
    class Meta:
        model = Incident
        fields = '__all__'
        exclude = ['date_created', ]

    def save(self, commit=True):
        obj = super(IncidentForm, self).save(commit=False)
        if obj.disciplinary_required == 0:
            obj.disciplinary_date = ''
            obj.called_by = ''

        obj.save()


User = get_user_model()


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        user = authenticate(username=username, password=password)

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("This user does not exist")
            if not user.check_password(password):
                raise forms.ValidationError("Incorrect password")
            if not user.is_active:
                raise forms.ValidationError("This user is not active")

        return super(UserLoginForm, self).clean(*args, **kwargs)
