from django.shortcuts import render, redirect, get_list_or_404
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

from .models import Post
from .forms import PostForm

class FrontPage(View):
    def get(self, request):
        posts = Post.objects.all()
        return render(request, 'core/frontpage.html', {'posts': posts})

class PostView(LoginRequiredMixin, View):
    def get(self, request):
        form = PostForm()
        return render(request, 'core/create_post.html', {'form':form})

    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            post = Post(created_by=request.user, text=text)
            post.save()
            return redirect('frontpage')


