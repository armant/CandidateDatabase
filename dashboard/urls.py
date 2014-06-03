from django.conf.urls import *
import views
from models import Candidates
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^add/$', views.add, name='add'),
    url(r'^update/(?P<pk>[\w-]+)/$', login_required(views.UpdateCandidate.as_view(), login_url='/login/'), name='update_candidate'),
    url(r'^delete/(?P<pk>[\w-]+)/$', login_required(views.DeleteCandidate.as_view(), login_url='/login/'), name='delete_candidate'),
)