from django.utils.translation import ugettext as _
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import Http404
from .forms import IncidentForm
from django.views.generic.edit import  UpdateView

from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,

)

from .forms import UserLoginForm
from .models import Incident


# from django.views.generic import View
# from .forms import UserForm

@login_required
def index(request):
    return render(request, 'wardens/wardens.html')


@login_required
def incident(request):
    return render(request, 'wardens/incident.html')


# def report(request):
#   return HttpResponse("this is the report form")

@login_required
def closed(request):
    return render(request, 'wardens/closed.html')


@login_required
def thankyou(request):
    return render(request, 'wardens/thankyou.html')


@login_required
def disciplinary_required(request):
    return render(request, 'wardens/required.html')


@login_required
def disciplinary_taken(request):
    return render(request, 'wardens/taken.html')


@login_required
def incident_form(request):
    form = IncidentForm(request.POST or None)

    # import pdb; pdb.set_trace()

    if form.is_valid():
        form.save()
        messages.success(request, _('Saved'))
        return redirect('incident_form')
    print form.errors
    return render(request, 'wardens/incident_form.html', {
        'form': form,
    })





def login_view(request):
    print(request.user.is_authenticated())
    title = "Login"
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")  # one has double quotations other has single?
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect("/wardens/")
    print(request.user.is_authenticated())  # not required in final project
    return render(request, "wardens/login.html", {"form": form, "title": title})


def logout_view(request):  # logs the user out and redirects to the 'thankyou' page
    logout(request)
    return redirect("/wardens/thankyou/")


@login_required
def cases(request):  # should work when reports are created
    results = Incident.objects.all()
    print results
    return render(request, "wardens/closed.html", {"results": results})

@login_required
def required(request):
    results = Incident.objects.all()
    print results
    return render(request, "wardens/required.html", {"results": results})

@login_required
def taken(request):
    results = Incident.objects.all()
    print results
    return render(request, "wardens/taken.html", {"results": results})

@login_required
def detail(request, pk):
    try:
        incident = Incident.objects.get(pk=pk)      #get object or 404? reduce amounts of code
    except Incident.DoesNotExist:
        raise Http404("report does not exist")
    return render(request, 'wardens/detail.html', {'incident': incident})


@login_required
def update(request, pk=None):
    instance = get_object_or_404(Incident, pk=pk)
    form = IncidentForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save()
        instance.save()

    context = {
        "title" : instance.title,
        "instance" : instance,
        "form" : form,
    }
    return render(request, "wardens/incident_form.html", context)