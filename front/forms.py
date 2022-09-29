from django import forms
from django.forms import ModelForm
from .models import Story

class Story_Form(forms.ModelForm):
    class Meta:
        model = Story
        fields=['post_date','approved_date','journalist_name','category','title','story','pic_1','pic_2','pic_3','approval_status']
        widgets = {
            'title': forms.TextInput(attrs={'size': '70'}),
        }