from django.db import models
import datetime


# Create your models here.
class AllData(models.Model):
    name = models.CharField(max_length=100)
    details = models.TextField(null=True, blank=True)
    date = models.DateTimeField(
        default=datetime.datetime.now,
        null=True,
        blank=True
    )
