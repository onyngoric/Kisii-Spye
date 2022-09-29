from datetime import datetime
from django.db import models
from django.utils import timezone


# Create your models here.
class Story(models.Model):
    post_date= models.DateTimeField(default=datetime.now, blank=True)
    approved_date= models.DateTimeField(default=datetime.now, blank=True)
    journalist_name= models.CharField(blank=True, max_length=200)
    STORY_CHOICES = [
        ('Choose option:', 'Choose option:'),
        ('Politics', 'Politics'),
        ('Social', 'Social'),
        ('Sports', 'Sports'),
        ('Entertainment', 'Entertainment'),
        ('More', 'More'),
    ]
    category= models.CharField(max_length=50,choices=STORY_CHOICES, default="Choose option")
    title= models.CharField(blank=True, max_length=50)
    story= models.TextField(blank=True)
    pic_1= models.ImageField(upload_to='images')
    pic_2= models.ImageField(upload_to='images')
    pic_3= models.ImageField(upload_to='images')
    approval_status= models.BooleanField(default=False)
    
    class Meta:
        verbose_name = ("Story")
        verbose_name_plural = ("Stories")
    
    def save(self, *args, **kwargs):
    #On save, update timestamps
        if not self.id:
            self.post_date = timezone.now()
        self.approved_date = timezone.now()
        return super(Story, self).save(*args, **kwargs)
    
    