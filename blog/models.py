from django.db import models

# Create your models here.
class Blog(models.Model):
    tytul = models.CharField(max_length=250)
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.tytul