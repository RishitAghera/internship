from django.conf.urls import url
from django.urls import path
from . import views

app_name='music'

urlpatterns=[
    # music/
    path('',views.IndexView.as_view(),name='index'),

    #music/930/
    url(r'^(?P<pk>[0-9]+)/*$',views.DetailView.as_view(),name='detail'),

    #music/album/add/
    url(r'album/add/$',views.AlbumCreate.as_view(),name='album-add'),

    #music/album/2
    url(r'album/(?P<pk>[0-9]+)/$',views.AlbumUpdate.as_view(),name='album-update'),


    #music/album/2/delete/
    url(r'album/(?P<pk>[0-9]+)/delete/$',views.AlbumDelete.as_view(),name='album-delete'),

    # music/songs/
    url(r'^songs/$',views.AllAlbum.as_view(),name='allsongs'),

    #music/song/add/
    url(r'song/add/$',views.SongCreate.as_view(),name='song-add'),

]