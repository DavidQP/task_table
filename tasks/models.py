from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200)

    def __str__(self):
        return f"{self.title}: {self.description}"