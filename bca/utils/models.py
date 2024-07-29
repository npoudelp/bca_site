from django.db import models
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys
from io import BytesIO
from PIL import Image
import os
from math import floor, ceil
from django.core.files.base import ContentFile

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


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    photo = models.ImageField(upload_to='teachers_image/' , blank=True, null=True)
    cv = models.FileField(upload_to='teachers_cv/' , blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class AboutBca(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=False, null=False)
    designation = models.CharField(max_length=100, blank=True, null=True)
    courtesy = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


    
# compress image
def compress(image):
    im = Image.open(image)
    im_io = BytesIO() 
    im.save(im_io, 'JPEG', quality=50) 
    new_image = ContentFile(im_io.getvalue(), image.name)
    return new_image

class Images(models.Model):
    image = models.ImageField(upload_to='gallary/')
    image_title = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.image
    
    def save(self, *args, **kwargs):
        if self.image:
            self.image = compress(self.image)
        super(Images, self).save(*args, **kwargs)
