from django.shortcuts import render, redirect
from django.views import View
from .forms import LoginForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render
import time

# Create your views here.

# def user_login(request):

#   return render(request, "account/login.html", {}) # Unused
class LoginView(View):
    def get(self, request):
        form = LoginForm()  # Initialize an empty form
        return render(request, "account/login.html", {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['phone'], password=cd['password'])
            if user is not None:
                login(request, user)
                return redirect("admin:index")
            else:
                form.add_error("phone", "Invalid phone number or password.")
        else:
            form.add_error(None, "Invalid data. Please check your inputs.")

        return render(request, "account/login.html", {'form': form})