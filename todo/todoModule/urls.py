from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.userhome, name='userhome')
    # url(r'^$', include('UsrMgmtModule.urls')),
    # url(r'^', include('UsrMgmtModule.urls'))
]
