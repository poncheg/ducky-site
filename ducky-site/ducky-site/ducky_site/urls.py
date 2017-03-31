"""
Definition of urls for ducky_site.
"""

from django.conf.urls import include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from ducky_site import django_rocket
# admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', ducky_site.views.home, name='home'),
    # url(r'^ducky_site/', include('ducky_site.ducky_site.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('django_rocket.urls', namespace="django_rocket")),
]
