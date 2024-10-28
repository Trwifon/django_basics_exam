from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('furry_funnies.common.urls')),
    path('posts/', include('furry_funnies.posts.urls')),
    path('author/', include('furry_funnies.author.urls')),
]
