from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import About, Contact
from .serializers import AboutSerializer, ContactSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Profile
from .serializers import ProfileSerializer  


class AboutViewSet(ModelViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializer

class ContactViewSet(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    

