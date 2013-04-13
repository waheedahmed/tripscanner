from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from trips.views import home
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tripscanner.views.home', name='home'),
    # url(r'^tripscanner/', include('tripscanner.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
     url(r'^trips/', include('trips.urls')),
     url(r'^api/', include('api.urls')),
     url(r'^$', home, name='home'),
     url(r'^home/?$', home,name='home'),
)
