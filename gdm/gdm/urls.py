from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
		url(r'^sistema/', include('sistema.urls', namespace="sistema")),
		url(r'^admin/', include(admin.site.urls))
)
