from django.db import models


class MyWatchList(models.Model):
    watched = models.BooleanField()
    title = models.CharField(max_length=255)
    rating = models.IntegerField()
    description = models.CharField(max_length=255)
    release_date = models.CharField(max_length=255)
    review = models.CharField(max_length=255)
