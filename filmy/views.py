from random import randint

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DetailView

from filmy.forms import AddPersonForm, AddMovieForm, AddCommentForm
from filmy.models import Person, Film, Category, Comment


class AddPersonView(View):

    def test_func(self):
        return self.request.user.is_superuser

    def get(self, request):
        form = AddPersonForm()
        return render(request, 'add_object.html', {'form': form})

    def post(self, request):
        form = AddPersonForm(request.POST, request.FILES)
        if form.is_valid():
            # first_name = form.cleaned_data['first_name']
            # last_name = form.cleaned_data['last_name']
            # Person.objects.create(first_name=first_name,
            #                       last_name=last_name)
            form.save()

        return render(request, 'add_object.html', {'form': form})


class AddMovieView(LoginRequiredMixin, View):

    def get(self, request):
        form = AddMovieForm()
        return render(request, 'add_object.html', {'form': form})

    def post(self, request):
        form = AddMovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('add_movie'))
        return render(request, 'add_object.html', {'form': form})


class AddCategoryView(LoginRequiredMixin, CreateView):
    model = Category
    template_name = 'add_object.html'
    fields = '__all__'
    success_url = reverse_lazy('add_category')

    # def get_form_class(self):
    # def get_form(self, form_class=None):
    #     super().get_form()
    # def form_valid(self, form):
    #     super().form_valid()
    # def form_invalid(self, form):
    # def get_success_url(self):
    # def get_context_data(self, **kwargs):
    # def get_object(self, queryset=None):


class MovieListView(PermissionRequiredMixin, ListView):
    permission_required = ['filmy.view_film']
    model = Film
    template_name = 'Film_list_view.html'


class MovieUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ['filmy.change_film']

    model = Film
    template_name = 'add_object.html'
    fields = '__all__'

    # def get_queryset(self):

    def get_success_url(self):
        super().get_success_url()
        return reverse("update_movie", args=(self.object.id,))


class MovieDetailView(DetailView):
    model = Film
    template_name = 'filmy/film_detail_view.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        form = AddCommentForm()
        data.update({'form': form, 'ptaszek': 'sikorka'})
        return data


class AddCommentView(View):
    def post(self, request, pk_movie):
        form = AddCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            movie = Film.objects.get(pk=pk_movie)
            user = request.user
            comment.author = user
            comment.movie = movie
            comment.save()
            return redirect('detail_movie', pk_movie)


class AddCommentGenericView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['text']

    def get_success_url(self):
        pk_movie = self.kwargs['pk_movie']
        return reverse('detail_movie', args=(pk_movie,))

    def form_valid(self, form):
        self.object = form.save(commit=False)
        pk_movie = self.kwargs['pk_movie']
        movie = Film.objects.get(pk=pk_movie)
        user = self.request.user
        self.object.author = user
        self.object.movie = movie
        self.object.save()
        return super(CreateView, self).form_valid(form)
