"""game URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import include, url
from django.urls import path
from django.contrib import admin
from mysite.views import *
from mysite import views


import mysite.views

urlpatterns = [
    url(r'^$', homePage),
    url(r'^startGame/', startGame, name="startGame"),
    url(r'^admin/', admin.site.urls),
    url(r'^selectCharactor/', views.selectCharactor, name="selectCharactor"),
    url(r'^gameIntroduction/', views.gameIntroduction, name="gameIntroduction"),
    url(r'^teamIntroduction/', views.teamIntroduction, name="teamIntroduction"),
    url(r'^settings1/', views.settings1, name="settings1"),
    url(r'^settings2/', views.settings2, name="settings2"),
    url(r'^settings3/', views.settings3, name="settings3"),
    url(r'^settings4/', views.settings4, name="settings4"),

]
