from django.conf.urls import patterns, include, url

urlpatterns = patterns('komensky.courses.views',
    url(r'^$', 'courses', name='courses'),
    url(r'^new/$', 'new_course', name='new_course'),
    url(r'^(\d+)/modulo/$', 'new_module', name='new_module'),
    url(r'^(\d+)/$', 'course', name='course'),
)