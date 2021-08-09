from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.


class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    ingridents = models.CharField(max_length=500, null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    steps = models.CharField(max_length=500, null=True, blank=True)
    cook_time = models.DecimalField(max_digits=7, decimal_places=2)
    _id = models.AutoField(primary_key=True, editable=False)
    steps = models.CharField(max_length=500, null=True, blank=True)
    #group = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title
