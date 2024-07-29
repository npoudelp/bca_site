from django import forms
from .models import Notice, HODmessage, BannerImage, Resource, Teacher, Images, AboutBca

class NoticeForm(forms.ModelForm):
    class Meta:
        model = Notice
        fields = ['title','file']


class HODmessageForm(forms.ModelForm):
    class Meta:
        model = HODmessage
        fields = ['name','message','photo']
    
    
class BannerImageForm(forms.ModelForm):
    class Meta:
        model = BannerImage
        fields = ['image']


class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ['title','file']


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['name','designation','phone','email','photo','cv']
        

class ImageForm(forms.ModelForm):
    class Meta:
        model = Images
        fields = ['image', 'image_title']


class AboutBcaForm(forms.ModelForm):
    class Meta:
        model = AboutBca
        fields = ['title', 'description', 'courtesy', 'designation']