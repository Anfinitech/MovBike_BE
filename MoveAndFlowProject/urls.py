"""MoveAndFlowProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from MoveAndFlowApp import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from MoveAndFlowApp.views.userView import UserRegisterView, UserAllView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('estaciones/', views.EstacionAllAndCreateView.as_view()),
    path('estaciones/<int:pk>/', views.EstacionSingularView.as_view()),
    
    path('bicicletas/', views.BicicletaAllAndCreateView.as_view()),
    path('bicicletas/<int:pk>/', views.BicicletaSingularView.as_view()),
    
    path('register/', UserRegisterView.as_view()),
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('users/', UserAllView.as_view()),
]
