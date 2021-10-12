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
from MoveAndFlowApp import views as MnFViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('estaciones/new/', MnFViews.EstacionCreateView.as_view()),
    path('estaciones/<int:pk>/', MnFViews.EstacionDetailView.as_view()),
    path('estaciones/all/', MnFViews.EstacionesView.as_view()),
    path('estaciones/upd/<int:pk>/', MnFViews.EstacionUpdateView.as_view()),
    path('estaciones/del/<int:pk>/', MnFViews.EstacionDeleteView.as_view()),
    
    path('bicicletas/new/', MnFViews.BicicletaCreateView.as_view()),
    path('bicicletas/<int:pk>/', MnFViews.BicicletaDetailView.as_view()),
    path('bicicletas/location/<int:estacion>/', MnFViews.BicicletaEstacionView.as_view()),
    path('bicicletas/upd/<int:pk>/', MnFViews.BicicletaUpdateView.as_view()),
    path('bicicletas/del/<int:pk>/', MnFViews.BicicletaDeleteView.as_view()),
]
