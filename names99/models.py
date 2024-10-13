from django.db import models

class NameOfAllah(models.Model):
    name = models.CharField(max_length=100)
    meaning = models.TextField()
    full_meaning = models.TextField()

    def __str__(self):
        return self.name


class NameOfAllah(models.Model):
    name = models.CharField(max_length=100)
    meaning = models.TextField()
    full_meaning = models.TextField(blank=True)
    read = models.BooleanField(default=False)  # This field tracks read status



    def __str__(self):
        return self.name