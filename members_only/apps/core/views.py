from django.shortcuts import render, redirect, get_list_or_404
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

from .models import Post
from .forms import PostForm

import re


def create_tagged_post_context(posts):
    def split_tagged_post(text):
        p = re.compile('(@[\w_\-!]+)')
        text = re.split(p, text)
        return text
   
    context = {
            'posts':[]
        }

    for post in posts:
        textlist = split_tagged_post(post.text)

        tagged_text = []

        for s in textlist:
            if s and s[0]=='@':
                qset = User.objects.filter(username=s[1:])
                if qset:
                    tagged_text.append({'text': s, 'tag': qset[0]}) 
                else:
                    tagged_text.append({'text': s, 'tag': None})
            else:
                tagged_text.append({'text': s, 'tag': None})

        context['posts'].append({'post': post, 'tagged_text': tagged_text})
    return context




class FrontPage(View):
    def get(self, request):
        posts = Post.objects.all()
        context = create_tagged_post_context(posts)
        return render(request, 'core/frontpage.html', context)

def get_tags_or_none(text):
    p = re.compile('(?<=@)\S+')
    tags = re.findall(p, text)
    return tags

class PostView(LoginRequiredMixin, View):
    def get(self, request):
        form = PostForm()
        return render(request, 'core/create_post.html', {'form':form})

    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            tags = get_tags_or_none(text)

            post = Post(created_by=request.user, text=text)
            post.save()

            users = []
            for tag in tags:
                qset = User.objects.filter(username=tag)
                if qset:
                    users.append(qset[0])
            
            post.tags.add(*users)
            post.save()

            return redirect('frontpage')


