"""songcrud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from musicapp import views 
# from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    
] 
urlpatterns = [
    path("admin/", admin.site.urls),
    path("songs/create/", views.CreateSong.as_view(), name="api_create"),
    path("songs/update/<int:pk>", views.UpdateSong.as_view(), name="api_update"),
    path("songs/delete/<int:pk>", views.DeleteSong.as_view(), name="api_delete"),
    path("songs/", views.SongList.as_view(), name="api_list"),
    path("songs/<int:pk>", views.SongDetails.as_view(), name="api-details"),
    path("artistes/", views.ArtisteList.as_view(), name="api_list"),
]
# urlpatterns = format_suffix_patterns(urlpatterns)