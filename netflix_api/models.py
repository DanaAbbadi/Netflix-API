from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Netflix(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete= models.CASCADE)
    series      = models.CharField(max_length=64)
    movie      = models.CharField(max_length=64)
    episode   = models.CharField(max_length=64)
    season    = models.CharField(max_length=64)

    def __str__(self):
        return self.line
