from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'komensky.core.views.home', name='home'),
)
