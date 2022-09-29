"""Kisii_Spye URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from turtle import home
from django.contrib import admin
from django.urls import path
from front import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('politics/', views.politics, name='politics'),
    path('post/', views.post_a_story.as_view(), name='post'),
    path('story/', views.story_page, name='story'),
    path('approve/',views.approve_story,name='approve'),
    path('social/', views.social, name='social'),
    path('entertainment/', views.entertainment, name='entertainment'),
    path('sports/', views.sports, name='sports'),
    path('more/', views.more, name='more'),
    path('login/', views.journalist_login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('logout_admin/', views.logout_admin, name='logout_admin'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

# customizing Django Site Title & Header
admin.site.site_header = 'Kisii Spye News Admin Panel'
admin.site.site_title = 'Kisii Spye News'
