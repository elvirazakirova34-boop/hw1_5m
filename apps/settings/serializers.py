from rest_framework import serializers
from .models import About, Contact
from .models import Profile, CompanyInfo
from apps.user.models import User

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class CompanyInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyInfo
        fields = ['title', 'content']

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__' 