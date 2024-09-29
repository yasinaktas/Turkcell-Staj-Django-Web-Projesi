from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    id_admin = models.BooleanField(default=False)
    id_deleted = models.BooleanField(default=False)