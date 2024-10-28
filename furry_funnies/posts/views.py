from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, FormView
from django.views.generic.edit import ProcessFormView

from furry_funnies.common.helpers import get_profile_object
from furry_funnies.posts.forms import CreatePostForm, EditPostForm, DeletePostForm
from furry_funnies.posts.models import Post


class CreatePostView(CreateView):
    model = Post
    template_name = 'posts/create-post.html'
    form_class = CreatePostForm
    success_url = reverse_lazy('dashboard')


    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        form.fields['title'].widget.attrs['placeholder'] = 'Put an attractive and unique title...'
        form.fields['content'].widget.attrs['placeholder'] = 'Share some interesting facts about your adorable pets...'

        return form


    def form_valid(self, form):
        form.instance.author = get_profile_object()
        return super().form_valid(form)


class DetailsPostView(DetailView):
    model = Post
    template_name = 'posts/details-post.html'
    pk_url_kwarg = 'post_id'


class EditPostView(UpdateView):
    model = Post
    template_name = 'posts/edit-post.html'
    form_class = EditPostForm
    pk_url_kwarg = 'post_id'
    success_url = reverse_lazy('dashboard')


class DeletePostView(DeleteView):
    model = Post
    template_name = 'posts/delete-post.html'
    form_class = DeletePostForm
    pk_url_kwarg = 'post_id'
    success_url = reverse_lazy('dashboard')

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)


