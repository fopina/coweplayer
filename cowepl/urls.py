from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^vote/(?P<music_id>\d+)/$', views.vote_up, name='vote_up'),
    url(r'^add/$', views.add_music, name='add'),
)
