from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

class Signup(View):
    def get(self, request):
        f = UserCreationForm()
        return render(request, 'accounts/signup', name='signup')

    def post(self, request):
        f = UserCreationForm(request.POST)
        if f.is_valid()
            user = f.save()
            login(requst, user)
        return redirect('frontpage')


