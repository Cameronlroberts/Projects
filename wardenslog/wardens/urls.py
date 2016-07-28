from django.conf.urls import url
from . import views
from wardens.views import (login_view, logout_view)

urlpatterns = [
    # url(r'^log$', views.UserFormView.as_view(), name='log'),       #Currently after wardens page i.e /wardens/log
    url(r'^$', views.index, name='index'),
    url(r'^incident/$', views.incident, name='incident'),
    url(r'^incident/form/$', views.incident_form, name='incident_form'),  # incident or form? better naming?
    url(r'^cases/$', views.cases, name='closed'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^thankyou/$', views.thankyou, name='logout'),
    url(r'^required/$', views.required, name='required'),
    url(r'^taken/$', views.taken, name='taken'),
    url(r'^detail/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    url(r'^update/(?P<pk>[0-9]+)/$', views.update, name='update'),

]
