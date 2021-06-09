from django.db import models
from django.utils import timezone
# Create your models here.


class Post(models.Model):
    postTitle = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    pw = models.CharField(max_length=15, default="password")
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"name : { self.name } , title: {self.postTitle}, content: {self.content[:10]}"

