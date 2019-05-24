from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Phone_Book(models.Model):
    Name = models.CharField(max_length=50)
    Number = models.CharField(max_length=14)
    Author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.Name

    def get_absolute_url(self):
        return reverse('file-detail', kwargs={'pk': self.pk})