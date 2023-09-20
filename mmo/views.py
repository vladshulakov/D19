from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from django.contrib.auth.decorators import login_required
from .models import Post, Reply


class PostList(ListView):
    model = Post
    ordering = '-time_create'
    template_name = 'posts.html'
    context_object_name = 'posts'
    paginate_by = 10

class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'

class ReplyDetail(DetailView):
    model = Reply
    template_name = 'reply.html'
    context_object_name = 'reply'

class ReplyList(ListView):
    model = Reply
    template_name = 'replys.html'
    ordering = '-time_create'
    context_object_name = 'replys'