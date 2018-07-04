from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="Profile")
    description = models.TextField()
    image = models.ImageField(upload_to="avatars", null=False, default='no_image.jpg')
    
    def __str__(self):
        return self.user.username