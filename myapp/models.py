from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class event(models.Model):
    event_name = models.CharField(max_length=255)
    event_image = models.ImageField(upload_to='images/')
    date = models.DateField()
    time = models.TimeField()
    address_line = models.CharField(max_length=400, blank=True, null=True)
    city = models.CharField(max_length=400, blank=True, null=True)
    state = models.CharField(max_length=400, blank=True, null=True)
    zipcode = models.CharField(max_length=10, blank=True, null=True)
    is_liked = models.BooleanField(default=False)
    def __str__(self):
        return self.title