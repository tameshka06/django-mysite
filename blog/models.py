from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to="images/", blank=True, null=True)
    video = models.FileField(upload_to="videos/", blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # вот это важно
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
