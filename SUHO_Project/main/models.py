from django.db import models

# Create your models here.
class Menu(models.Model):
    menuName = models.CharField(max_length=100)
