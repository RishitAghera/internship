from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Album, Song


class IndexView(generic.ListView):
    template_name = 'music/index.html'

    def get_queryset(self):
        return Album.objects.all()


class DetailView(generic.DetailView):
    model =  Album
    template_name = 'music/detail.html'

class AlbumCreate(CreateView):
    model = Album
    fields= ['artist','album_title','genre','album_logo']

class AlbumDelete(DeleteView):
    model= Album
    success_url = reverse_lazy('music:index')

class AlbumUpdate(UpdateView):
    model = Album
    fields= ['artist','album_title','genre','album_logo']

class AllAlbum(generic.ListView):
    template_name = 'music/allsongs.html'

    def get_queryset(self):
        return Album.objects.all()

class SongCreate(CreateView):
    model= Song
    fields = ['album','files_type','song_title']
    success_url = reverse_lazy('music:allsongs')