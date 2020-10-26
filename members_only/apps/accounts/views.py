from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .models import Profile
from apps.core.models import Post
from apps.core.views import create_tagged_post_context


class Signup(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'accounts/signup.html', {'form': form})
        

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
        return redirect('frontpage')


class ProfileView(View):
    def get(self, request, username):
        user = get_object_or_404(User, username=request.user.username)
        profile = get_object_or_404(User, username=username)
        posts = profile.posts.all()
        context = create_tagged_post_context(posts)
        context['user'] = user
        context['profile'] = profile

        return render(request, 'accounts/profile.html', context)