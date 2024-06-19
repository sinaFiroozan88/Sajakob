from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='authors/', blank=True)

    def __str__(self):
        return self.name
