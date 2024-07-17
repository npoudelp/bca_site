from django.db import models

# Create your models here.

class Notice(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to='notices/' , blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class HODmessage(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField(blank=False, null=False)
    photo = models.ImageField(upload_to='hodmessages/' ,blank=False, null=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.date


class BannerImage(models.Model):
    image = models.ImageField(upload_to='bannerimages/' ,blank=False, null=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.date
    

class Resource(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='resources/' , blank=False, null=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title