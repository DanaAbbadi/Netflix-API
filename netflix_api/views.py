from django.shortcuts import render
from rest_framework import generics

from .permissions import IsAuthorOrReadOnly
from .models import Netflix
from .serializer import NetflixSerializer
from rest_framework import permissions
# Create your views here.

class NetflixList(generics.ListCreateAPIView):
    queryset = Netflix.objects.all()
    serializer_class = NetflixSerializer

class NetflixDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Netflix.objects.all()
    serializer_class = NetflixSerializer
