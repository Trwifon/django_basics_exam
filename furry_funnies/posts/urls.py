from django.urls import path, include

from furry_funnies.posts.views import CreatePostView, DetailsPostView, EditPostView, DeletePostView

urlpatterns = [
    path('create/', CreatePostView.as_view(), name='create_post'),
    path('<int:post_id>/', include([
        path('details/', DetailsPostView.as_view(), name='details_post'),
        path('edit/', EditPostView.as_view(), name='edit_post'),
        path('delete/', DeletePostView.as_view(), name='delete_post'),
    ]))
    # path('dashboard/', dashboard, name='dashboard'),

]