from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.UserHome.as_view(), name='userhome')
    # url(r'^$', include('UsrMgmtModule.urls')),
    # url(r'^', include('UsrMgmtModule.urls'))
]
