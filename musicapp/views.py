from django.shortcuts import render
from .models import Song, Artiste
from rest_framework import generics
from .serializers import SongSerializer, ArtisteSerializer
# Create your views here.
class SongList(generics.ListAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
class ArtisteList(generics.ListAPIView):
    queryset = Artiste.objects.all()
    serializer_class = ArtisteSerializer
class CreateSong(generics.CreateAPIView):
    queryset = Song.objects
    serializer_class = SongSerializer

class SongDetails(generics.RetrieveAPIView):
    queryset = Song.objects
    serializer_class = SongSerializer

class UpdateSong(generics.UpdateAPIView):
    queryset = Song.objects.filter()
    serializer_class = SongSerializer

class DeleteSong(generics.DestroyAPIView):
    queryset = Song.objects.filter()
    serializer_class = SongSerializer