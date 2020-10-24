from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    created_on = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

    class Meta:
        ordering = ['-created_on']