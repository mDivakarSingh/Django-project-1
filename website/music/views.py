from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Album


# Create your views here.

def index(request):
    all_album= Album.objects.all()
    context= {'all_album': all_album}
    return render(request, 'music/index.html', context,)

def detail(request, album_id):

    album = get_object_or_404(Album, pk=album_id)

    # try:
    #     album = Album.objects.get(pk=album_id)
    # except Album.DoesNotExist:
    #     raise Http404("Does not exist")

    return render(request, 'music/detail.html', {'album':album})
