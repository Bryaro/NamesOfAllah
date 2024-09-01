from django.db import models

class NameOfAllah(models.Model):
    day_number = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    transliteration = models.CharField(max_length=100)
    meaning = models.CharField(max_length=255)

    def __str__(self):
        return self.name
