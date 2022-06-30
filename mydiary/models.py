from django.db import models

# Create your models here.

class Diary(models.Model):
    text = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
