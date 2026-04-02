from rest_framework.routers import DefaultRouter
from django.urls import path
from apps.user.views import RegisterAPI, CustomToken
from django.urls import path
from .views import MyProfileAPIView

router = DefaultRouter()
router.register("register", RegisterAPI, basename="register")

urlpatterns = [
    
]
from rest_framework_simplejwt.views import (
    TokenRefreshView, TokenBlacklistView
)
urlpatterns += router.urls
urlpatterns = [
    path("token/", CustomToken.as_view(), name="token"),
    path("token/refresh", TokenRefreshView.as_view(), name="refresh"),
    path("token/logout", TokenBlacklistView.as_view(), name="logout"),
]


urlpatterns = [
    path('profile/', MyProfileAPIView.as_view(), name='profile'),
]