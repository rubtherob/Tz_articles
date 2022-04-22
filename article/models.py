from django.conf import settings
from django.db import models

# Create your models here.



class Artcle(models.Model):
    text = models.TextField(max_length=200)
    time_create = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL,  on_delete=models.PROTECT)
    Private = models.BooleanField(default=False)