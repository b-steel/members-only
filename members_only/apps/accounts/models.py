from django.db import models

from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.ForeignKey(User, related_name='profile', on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

User.profile = property(lambda u: Profile.objects.get_or_create(user=u)[0
])