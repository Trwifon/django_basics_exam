
from django.shortcuts import render
from django.views.generic import ListView

from furry_funnies.posts.models import Post

from furry_funnies.furry_funnies.author.models import Author


def index(request):
    return render(request, 'common/index.html')


class Dashboard(ListView):
    model = Author
    template_name = 'common/dashboard.html'
    context_object_name = 'posts'
