from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    url(r'^upload/$', 'emily.main.views.upload_file', name='upload'),
    url(r'^$', 'emily.main.views.home', name='home'),
)