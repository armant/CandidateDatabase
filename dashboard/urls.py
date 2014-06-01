from django.conf.urls import patterns, include, url
import views
from models import Candidates

urlpatterns = patterns('',
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^add/$', views.add, name='add'),
)