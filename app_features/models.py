from django.db import models

# Create your models here.

class Features(models.Model):
    title = models.CharField(max_length=60)
    price = models.IntegerField()
    image_relative_url = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self) -> str:
        return '{} (id: {})'.format(self.title, self.id)