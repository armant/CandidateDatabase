from django.conf.urls import patterns, include, url
from dashboard import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^dashboard/', include('dashboard.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'django.contrib.auth.views.login', name="my_login"),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '../CandidateDatabase/media/'}),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^$', views.home_page, name="home_page"),
)
