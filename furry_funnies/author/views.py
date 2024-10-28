from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from furry_funnies.author.forms import CreateAuthorForm, EditAuthorForm
from furry_funnies.author.models import Author
from furry_funnies.common.helpers import get_profile_object
from furry_funnies.posts.models import Post


class CreateAuthorView(CreateView):
    model = Author
    template_name = 'author/create-author.html'
    form_class = CreateAuthorForm
    success_url = reverse_lazy('dashboard')

    def get_form (self, form_class = None):
        form = super().get_form(form_class=form_class)
        form.fields['first_name'].widget.attrs['placeholder'] = 'Enter your first name...'
        form.fields['last_name'].widget.attrs['placeholder'] = 'Enter your last name...'
        form.fields['passcode'].widget.attrs['placeholder'] = 'Enter 6 digits...'
        form.fields['pets_number'].widget.attrs['placeholder'] = 'Enter the number of your pets...'

        return form


class DetailsAuthorView(DetailView):
    model = Author
    template_name = 'author/details-author.html'
    context_object_name = 'author'

    def get_object(self):
        self.pk_url_kwarg = get_profile_object().pk
        return self.pk_url_kwarg

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        last_post = Post.objects.filter(author=self.pk_url_kwarg).order_by('updated_at').last()
        if last_post:
            context['last_post'] = last_post.title
        return context


class EditAuthorView(UpdateView):
    model = Author
    template_name = 'author/edit-author.html'
    form_class = EditAuthorForm
    success_url = reverse_lazy('details_author')

    def get_object(self):
        return get_profile_object()


class DeleteAuthorView(DeleteView):
    model = Author
    template_name = 'author/delete-author.html'
    success_url = reverse_lazy('index')

    def get_object(self):
        return get_profile_object()



