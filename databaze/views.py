from django.shortcuts import render
from databaze.models import Album, Umelec, Zanr, Song, Attachment
from django.views.generic import ListView, DetailView


def index(request):
    num_alba = Album.objects.all().count()
    alba = Album.objects.order_by('nazev_album')[:3]

    context = {
        'num_alba': num_alba,
        'alba': alba,
        'umelec': Umelec.objects.all(),
        'zanr': Zanr.objects.all()

    }
    return render(request, 'index.html', context=context)

class AlbumListView(ListView):
    model = Album
    context_object_name = 'album_list'
    template_name = 'album/list.html'

class AlbumDetailView(DetailView):
    model = Album
    context_object_name = 'album_detail'
    template_name = 'album/detail.html'


