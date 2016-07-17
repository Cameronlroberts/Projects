from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from .forms import IncidentForm

from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,

    )

from .forms import UserLoginForm


#from django.views.generic import View
#from .forms import UserForm


def index(request):
    return render(request, 'wardens/wardens.html')


# @permission_required('wardens.incident')
def incident(request):
    return render(request, 'wardens/incident.html')


# def report(request):
#   return HttpResponse("this is the report form")


def closed(request):
    return render(request, 'wardens/closed.html')


def log(request):
    return render(request, 'wardens/log.html')


def incident_form(request):
    form = IncidentForm(request.POST or None)

    if form.is_valid():
        return redirect('incident')

    return render(request, 'wardens/incident_form.html', {
        'form': form,
    })


def login_view(request):
    print(request.user.is_authenticated())
    title = "Login"
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")        #one has double quoatations other has single?
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        print(request.user.is_authenticated())

    return render(request, "wardens/form.html", {"form": form, "title": title})


def logout_view(request):
    logout(request)
    return render(request, "form.html", {})


