

from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import ListView, CreateView

from filmy.forms import AddPersonForm, AddMovieForm
from filmy.models import Person, Film, Category


class AddPersonView(View):

    def get(self, request):
        form = AddPersonForm()
        return render(request, 'add_object.html', {'form':form})

    def post(self, request):
        form = AddPersonForm(request.POST)
        if form.is_valid():
            # first_name = form.cleaned_data['first_name']
            # last_name = form.cleaned_data['last_name']
            # Person.objects.create(first_name=first_name,
            #                       last_name=last_name)
            Person.objects.create(**form.cleaned_data)
            form = AddPersonForm()

        return render(request, 'add_object.html', {'form': form})


class AddMovieView(View):

    def get(self, request):
        form = AddMovieForm()
        return render(request, 'add_object.html', {'form':form})

    def post(self, request):
        form = AddMovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('add_movie'))
        return render(request, 'add_object.html', {'form': form})


class AddCategoryView(CreateView):
    model = Category
    template_name = 'add_object.html'
    fields = '__all__'
    success_url = reverse_lazy('add_category')

    # def get_form_class(self):
    # def get_form(self, form_class=None):

class MovieListView(ListView):
    model = Film
    template_name = 'Film_list_view.html'
