from pickle import TRUE
from urllib import request
from django.shortcuts import render
from django.urls import reverse
from .models import Story
from .forms import Story_Form
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import logout
from django.shortcuts import redirect

# Create your views here.
def index(request):
   return render(request,'Kisii_Spye/index.html')
def politics(request):
   if request.method == 'POST':
      story_id = request.POST.get('id')
      request.session['story_session']= story_id
      return HttpResponseRedirect(reverse('story'))
   else:
      category = "Politics"
      story=Story.objects.all().filter(approval_status='1',category='Politics')
      return render(request,'Kisii_Spye/story_preview.html',{'story':story,'category':category})

def sports(request):
   if request.method == 'POST':
      story_id = request.POST.get('id')
      request.session['story_session']= story_id
      return HttpResponseRedirect(reverse('story'))
   else:
      category = "Sports"
      story=Story.objects.all().filter(approval_status='1',category='Sports')
      return render(request,'Kisii_Spye/story_preview.html',{'story':story,'category':category})

def social(request):
   if request.method == 'POST':
      story_id = request.POST.get('id')
      request.session['story_session']= story_id
      return HttpResponseRedirect(reverse('story'))
   else:
      category = "Social"
      story=Story.objects.all().filter(approval_status='1',category='Social')
      return render(request,'Kisii_Spye/story_preview.html',{'story':story,'category':category})

def entertainment(request):
   if request.method == 'POST':
      story_id = request.POST.get('id')
      request.session['story_session']= story_id
      return HttpResponseRedirect(reverse('story'))
   else:
      category = "Entertainment"
      story=Story.objects.all().filter(approval_status='1',category='Entertainment')
      return render(request,'Kisii_Spye/story_preview.html',{'story':story,'category':category})

def more(request):
   if request.method == 'POST':
      story_id = request.POST.get('id')
      request.session['story_session']= story_id
      return HttpResponseRedirect(reverse('story'))
   else:
      category = "More"
      story=Story.objects.all().filter(approval_status='1',category='More')
      return render(request,'Kisii_Spye/story_preview.html',{'story':story,'category':category})

@method_decorator(login_required, name='dispatch')
class post_a_story(TemplateView):
   template_name='Kisii_Spye/Post A Story.html'
   
   
   def get(self, request):
      form = Story_Form()
      get_username = request.session['username_sess']
      return render(request, self.template_name, {'form':form,'get_username':get_username})
    
   def post(self, request):
      if request.method == 'POST':
         form = Story_Form(request.POST, request.FILES)
         get_username = request.session['username_sess']
         if form.is_valid():
            form.save()
            messages.success(request, 'Story Submited successfuly')
            return render(request, self.template_name, {'form':form,'get_username':get_username})
         else:
            messages.warning(request, 'Submission failed, Please Retry.')
            return render(request, self.template_name, {'form':form,'get_username':get_username})  
   
def story_page(request):
   story_id = request.session['story_session']
   story = Story.objects.all().filter(id=story_id)
   return render(request,'Kisii_Spye/story page.html', {'story': story})

@login_required(login_url='admin_login')
def approve_story(request):
   if request.method == 'POST':
      story_id = request.POST.get('id')
      the_story=Story.objects.all().filter(id=story_id).update(approval_status="1") #UPDATE approval status to True
      story = Story.objects.all().filter(approval_status="0")
      messages.success(request, 'Story Approved')
      return render(request,'Kisii_Spye/Approve stories.html',{'story': story})
   elif request.method == 'GET':
      story_id = request.GET.get('id')
      the_story=Story.objects.all().filter(id=story_id).delete() #get the story with the corresponding id and delete
      story = Story.objects.all().filter(approval_status="0")
      return render(request,'Kisii_Spye/Approve stories.html',{'story': story})
   else:
      story = Story.objects.all().filter(approval_status="0")
      return render(request,'Kisii_Spye/Approve stories.html',{'story': story})
   
def journalist_login(request):
   request.session.clear()
   #render counter login page
   if request.method == 'POST':
      username = request.POST['username']
      password = request.POST['password']
      get_username = request.POST.get('username')
      request.session['username_sess']= get_username
      user = authenticate(request, username=username, password=password)
      if user is not None:
         login(request, user)
      return HttpResponseRedirect(reverse('post'))
   return render(request, 'Kisii_Spye/journalist_login.html')

def logout_view(request):
    logout(request)
    return redirect('login')
 
def admin_login(request):
   request.session.clear()
   #render counter login page
   if request.method == 'POST':
      username = request.POST['username']
      password = request.POST['password']
      get_username = request.POST.get('username')
      request.session['username_sess']= get_username
      user = authenticate(request, username=username, password=password)
      if user is not None: 
         if user.is_superuser is True:
            login(request, user)
         return HttpResponseRedirect(reverse('approve'),{'username':username})
      else:
         return render(request, 'Kisii_Spye/admin_login.html')
   else:
      return render(request, 'Kisii_Spye/admin_login.html')

def logout_admin(request):
    logout(request)
    return redirect('admin_login')