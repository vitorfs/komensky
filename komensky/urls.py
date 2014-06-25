from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'komensky.core.views.home', name='home'),
    url(r'^cursos/', include('komensky.courses.urls')),
)
