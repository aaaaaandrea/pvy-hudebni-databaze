from django.shortcuts import render
from databaze.models import Album, Umelec, Zanr, Attachment

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

# Create your views here.
