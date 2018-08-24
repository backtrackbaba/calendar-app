from django.db import models

# Create your models here.

class Entry(models.Model):

    name = models.CharField(max_length=100)
    date = models.DateTimeField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} {self.date}'