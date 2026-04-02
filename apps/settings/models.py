from django.db import models
from apps.user.models import User

class About(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title
    
class Contact(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()

    def __str__(self):
        return self.email
    
class CompanyInfo(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.title
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile' )

    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True, verbose_name='О себе')
    birth_date = models.DateField(null=True, blank=True, verbose_name='Дата рождения')

    def __str__(self):
        return f"Профиль пользователя: {self.user.username}"