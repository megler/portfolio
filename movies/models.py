from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255, unique=True, blank=False)
    year = models.IntegerField(blank=False)
    description = models.TextField(blank=False)
    rating = models.FloatField(blank=False, null=True)
    ranking = models.IntegerField(blank=False, null=True)
    review = models.TextField(blank=False, null=True)
    img_url = models.URLField(
        blank=False,
        unique=True,
    )
