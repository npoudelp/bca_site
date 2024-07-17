from django import forms
from .models import Notice, HODmessage, BannerImage, Resource

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