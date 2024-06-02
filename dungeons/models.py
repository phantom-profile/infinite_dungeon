from django.db import models


class Adventurer(models.Model):
    objects = models.QuerySet

    name = models.CharField(blank=False, null=False, max_length=200)
    uid = models.CharField(blank=False, null=False, max_length=100, unique=True)
    level = models.IntegerField(default=1, null=False)
