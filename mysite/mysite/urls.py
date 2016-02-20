"""
Definition of urls for site.
"""

from django.conf.urls import patterns, url

from django.conf.urls import include
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^app/', include('app.urls')),
)
