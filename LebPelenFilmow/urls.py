"""LebPelenFilmow URL Configuration

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
from django.urls import path
from django.views.generic import TemplateView

from filmy import views
from accounts import views as a_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='base.html'), name='index'),
    path('add_person/', views.AddPersonView.as_view(), name='add_person'),
    path('add_movie/', views.AddMovieView.as_view(), name='add_movie'),
    path('login/', a_views.LoginView.as_view(), name='login'),
    path('logout/', a_views.LogoutView.as_view(), name='logout'),
    path('create_user/', a_views.RegisterView.as_view(), name='add_user')
]
