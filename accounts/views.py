from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views import View

from accounts.forms import LoginForm, CreateUserForm


class LoginView(View):

    def get(self, request):
        return render(request, 'accounts/login.html', {'form': LoginForm()})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,
                                username=username,
                                password=password)
            if user is not None:
                login(request, user)
                url = request.GET.get('next', reverse('index'))
                return redirect(url)
        return render(request, 'accounts/login.html', {'form': LoginForm()})


class LogoutView(View):

    def get(self, request):
        logout(request)
        return redirect("index")


class RegisterView(View):

    def get(self, request):
        form = CreateUserForm()
        return render(request, 'accounts/create_user.html', {'form': form})

    def post(self, request):
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            return redirect('login')
        return render(request, 'accounts/create_user.html', {'form': form})
