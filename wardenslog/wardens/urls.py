from django.conf.urls import url
from . import views
from wardens.views import (login_view, logout_view)


urlpatterns = [
   # url(r'^log$', views.UserFormView.as_view(), name='log'),       #Currently after wardens page i.e /wardens/log
    url(r'^$', views.index, name='index'),
    url(r'^incident/$', views.incident, name='incident'),
    url(r'^incident/form/$', views.incident_form, name='incident_form'),     #incident or form? better naming?
    url(r'^closed/$', views.cases, name='closed'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^thankyou/$', views.thankyou, name='logout'),
    url(r'^required/$', views.disciplinary_required, name='required'),
    url(r'^taken/$', views.disciplinary_taken, name='taken'),


]