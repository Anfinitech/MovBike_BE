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
    path('estacion/', MnFViews.EstacionCreateView.as_view()),
    path('estacion/<int:pk>/', MnFViews.EstacionDetailView.as_view()),
    path('bicicleta/', MnFViews.BicicletaCreateView.as_view()),
    path('bicicleta/<int:pk>/', MnFViews.BicicletaDetailView.as_view()),
    path('bicicleta/location/<int:estacion>/', MnFViews.BicicletaEstacionView.as_view()),
    path('bicicleta/update/<int:pk>/', MnFViews.BicicletaUpdateView.as_view()),
    path('bicicleta/remove/<int:pk>/', MnFViews.BicicletaDeleteView.as_view()),
]
