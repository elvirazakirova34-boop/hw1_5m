from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import About, Contact
from .serializers import AboutSerializer, ContactSerializer

class AboutViewSet(ModelViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializer

class ContactViewSet(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer