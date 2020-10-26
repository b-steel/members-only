from django.shortcuts import render, redirect, get_list_or_404
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

from .models import Post

class FrontPage(View):
    def get(self, request):
        return render(request, 'core/frontpage.html', {})


