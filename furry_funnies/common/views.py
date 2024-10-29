
from django.shortcuts import render
from django.views.generic import ListView

from furry_funnies.furry_funnies.posts.models import Post


def index(request):
    return render(request, 'common/index.html')


class Dashboard(ListView):
    model = Post
    template_name = 'common/dashboard.html'
    context_object_name = 'posts'
