from rest_framework import mixins
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework_simplejwt.views import TokenObtainPairView  

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Profile
from .serializers import ProfileSerializer
from apps.user.models import User
from apps.user.serializers import RegisterSerializers, TokenObtainPairSerializer

class RegisterAPI(mixins.CreateModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterSerializers

class CustomToken(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer


class MyProfileAPIView(APIView):
    # Доступ только для залогиненных пользователей
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # request.user — это тот, кто сделал запрос
        profile = Profile.objects.get(user=request.user)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)