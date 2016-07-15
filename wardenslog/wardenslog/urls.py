

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^wardens/', include('wardens.urls')),
    url('^', include('django.contrib.auth.urls')),
]


