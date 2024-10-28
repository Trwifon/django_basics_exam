from django.urls import path

from furry_funnies.author.views import CreateAuthorView, DetailsAuthorView, EditAuthorView, DeleteAuthorView

urlpatterns = [
    path('create/', CreateAuthorView.as_view(), name='create_author'),
    path('details/', DetailsAuthorView.as_view(), name='details_author'),
    path('edit/', EditAuthorView.as_view(), name='edit_author'),
    path('delete/', DeleteAuthorView.as_view(), name='delete_author'),





]