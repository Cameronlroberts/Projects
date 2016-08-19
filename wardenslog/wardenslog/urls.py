

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^admin/', admin.site.urls),               #Make sure there URLs are ok
    url(r'^wardens/', include('wardens.urls')),
    url('^', include('django.contrib.auth.urls')),
]


