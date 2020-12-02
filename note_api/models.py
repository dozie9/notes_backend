from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Note(models.Model):
    title = models.CharField(max_length=100)
    note = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
