from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import IncidentForm

from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm


def index(request):
    return render(request, 'wardens/wardens.html')


# @permission_required('wardens.incident')
def incident(request):
    return render(request, 'wardens/incident.html')


#def report(request):
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

class UserFormView(View):
    form_class = UserForm
    template_name= 'wardens/log.html'

    #display blank form

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    #process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            #cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('index.view')
            return render(render, self.template_name, {'form': form})