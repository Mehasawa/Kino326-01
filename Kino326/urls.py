"""
URL configuration for Kino326 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from catalog import views
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('kino/all/', views.kinolist.as_view(), name='allkino'),
    # path('kino/<int:pk>/', views.kinodetail.as_view(),name='info'),
    path('kino/<int:pk>/', views.kinodetail, name='info'),
    path('director/all/', views.directorlist.as_view(), name='alldirector'),
    path('director/<int:pk>/', views.directordetail.as_view(), name='infodirector'),
    path('user/', include('django.contrib.auth.urls')),
    path('accounts/profile/', views.index),
    path('user/reg/',  views.reg, name='registration'),
    path('accounts/login/', views.index),
    path('podpiska/<int:userid>', views.topodpiska, name='podpiska'),
    # path('podpiska/plusbalance/', views.plusbalance,name='plusbalance')
]
