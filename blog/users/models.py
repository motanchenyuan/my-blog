from django.db import models
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    nickname = models.varchar(max_length=50, blank=True)
    
    class Meta(AbstractUser.Meta):
            pass


