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
from django.urls import path


from filmy import views

urlpatterns = [

    path('add_person/', views.AddPersonView.as_view(), name='add_person'),
    path('add_movie/', views.AddMovieView.as_view(), name='add_movie'),
    path('update_movie/<int:pk>/', views.MovieUpdateView.as_view(), name='update_movie'),
    path('movie/<int:pk>/', views.MovieDetailView.as_view(), name='detail_movie'),
    path('movie/<int:pk_movie>/add_coment/', views.AddCommentView.as_view(), name='add_comment'),
    path('movie/<int:pk_movie>/add_coment_generic/', views.AddCommentGenericView.as_view(), name='add_comment_generic'),
    path('add_category/', views.AddCategoryView.as_view(), name='add_category'),
    path('movie_list/', views.MovieListView.as_view(), name='movie_list'),
]
