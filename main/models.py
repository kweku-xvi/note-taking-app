from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User 

class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='note', null=True)
    title = models.CharField(max_length=1000)
    content = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home-page')
