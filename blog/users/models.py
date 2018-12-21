from django.db import models
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    nickname = models.CharField(max_length=50, blank=True)
     list_display = ("Email address，")
    class Meta(AbstractUser.Meta):
            pass


