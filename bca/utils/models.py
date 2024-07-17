from django.db import models

# Create your models here.

class Notice(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    file = models.FileField(upload_to='notices/')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
