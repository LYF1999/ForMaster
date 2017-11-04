from django.db import models


# Create your models here.


class ActionSeries(models.Model):
    name = models.CharField(max_length=255, blank=True, unique=True)
    desc = models.TextField()


class Action(models.Model):
    series = models.ForeignKey(ActionSeries)
    video = models.FileField(null=True, blank=True)

