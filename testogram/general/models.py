from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    friends = models.ManyToManyField(
        to="self",
        symmetrical=True,
        blank=True,
    )
    
class Post (models.Model):
    author = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name="posts",
    )
    title = models.Charfield(max_length=64)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)