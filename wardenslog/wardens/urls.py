from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^log$', views.UserFormView.as_view(), name='log'),       #Currently after wardens page i.e /wardens/log
    url(r'^$', views.index, name='index'),
    url(r'^incident/$', views.incident, name='incident'),
    url(r'^incident/form/$', views.incident_form, name='incident_form'),     #incident or form? better naming?
    url(r'^closed/$', views.closed, name='closed'),

]