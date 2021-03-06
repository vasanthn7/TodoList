from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.UserHome.as_view(), name='userhome'),
    url(r'^deleted/', views.Deleted.as_view(), name='deleted'),
    url(r'^done/(?P<pk>\d+)/$', views.statusdone, name='statusdone'),
    url(r'^softdelete/(?P<pk>\d+)/$', views.softdelete, name='softdelete'),
    url(r'^restore/(?P<pk>\d+)/$', views.restore, name='restore'),
    url(r'^permdelete/(?P<pk>\d+)/$', views.permdelete, name='permdelete'),
    url(r'^datefilter/(?P<pk>\d+)/$', views.datefilter, name='datefilter'),
    url(r'^search/', views.searchtitle, name='searchtitle'),
    # url(r'^search/search', views.searchtitle_redirect, name='searchtitle_redirect'),

    # url(r'^titlesearch/(?P<name>\w+)/$', views.titlesearch, name='titlesearch'),
    # url(r'^$', include('UsrMgmtModule.urls')),
    # url(r'^', include('UsrMgmtModule.urls'))
]
