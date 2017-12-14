from django.conf.urls import url, include

from . import views

from django.conf.urls import include
from rest_framework import routers, serializers, viewsets

from .models import Word, WordTL
from . import serializers

router = routers.DefaultRouter()
router.register(r'words2k', serializers.WordViewSet, '2k')
router.register(r'words5k', serializers.MoreWordViewSet,' 5k')

app_name = 'dict'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^api/', include(router.urls)),
    url(r'^w/$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^s/[^\S\n\t]*(?P<word>[\S]+)[^\S\n\t]*/$', views.search, name='search'),
    url(r'^w/(?P<word>[\S]+)/$', views.detail, name='detail'),
    #maybe add namespaces someday / nah, nope
]
