from django.conf.urls import url, include
from . import views
from django.contrib.auth.views import login,logout



urlpatterns = [
    url(r'^$', views.home),
    url(r'^login/$', login,{'template_name': 'UsrMgmtModule/login.html'}),
    url(r'^logout/$', logout,{'template_name': 'UsrMgmtModule/logout.html'}),
    url(r'^register/$', views.register, name='register'),
    url(r'profile/', include('todoModule.urls')),
]
