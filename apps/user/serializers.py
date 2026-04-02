
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from apps.user.models import User
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile

class RegisterSerializers(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            "id", "email", "fiest_name", "last_name",
            "password"
        ]

    def create(self, validated_date):
        return User.objects.create_user(**validated_date)
    
class TokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        data["user_id"] = self.user.id
        data["email"] = self.user.email
        return data
    

class UserSerializer(serializers.ModelSerializer):
    bio = serializers.CharField(source='profile.bio', read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'bio']

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = ['user', 'avatar', 'bio', 'birth_date']