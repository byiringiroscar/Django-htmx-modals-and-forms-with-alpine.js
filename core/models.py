from django.db import models

# Create your models here.

class Complaint(models.Model):
    text = models.TextField()
    email = models.EmailField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
