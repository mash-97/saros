from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

from posts.models import *
from posts.forms import *
class PostList(ListView):
    template_name = 'posts/posts.html'
    model = Post 
    context_object_name = "posts"

class PostCreate(CreateView):
    template_name = 'posts/post_create.html'
    form_class = PostForm 
    success_url = reverse_lazy('home') 

    def form_valid(self, form):
        form.instance.user = self.request.user 
        return super(PostCreate, self).form_valid(form) 
    

class PostDetail(DetailView):
    template_name = 'posts/post_detail.html'
    model = Post 
    context_object_name = "post"
