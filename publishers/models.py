from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to="logos", blank=True)

    def __str__(self):
        return self.name