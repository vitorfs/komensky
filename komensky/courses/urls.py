from django.conf.urls import patterns, include, url

urlpatterns = patterns('komensky.courses.views',
    url(r'^$', 'courses', name='courses'),
)