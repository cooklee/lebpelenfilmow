from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

from filmy.forms import AddPersonForm, AddMovieForm
from filmy.models import Person


class AddPersonView(View):

    def get(self, request):
        form = AddPersonForm()
        return render(request, 'add_person.html', {'form':form})

    def post(self, request):
        form = AddPersonForm(request.POST)
        if form.is_valid():
            # first_name = form.cleaned_data['first_name']
            # last_name = form.cleaned_data['last_name']
            # Person.objects.create(first_name=first_name,
            #                       last_name=last_name)
            Person.objects.create(**form.cleaned_data)
            form = AddPersonForm()

        return render(request, 'form.html', {'form': form})


class AddMovieView(View):

    def get(self, request):
        form = AddMovieForm()
        return render(request, 'form.html', {'form':form})

    def post(self, request):
        form = AddMovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_movie')
        return render(request, 'form.html', {'form': form})




