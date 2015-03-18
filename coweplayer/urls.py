from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'', include('cowepl.urls', namespace = 'cowepl')),
)
