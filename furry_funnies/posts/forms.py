from django import forms

from furry_funnies.posts.apps import PostsConfig
from furry_funnies.posts.mixins import ReadonlyViewMixin
from furry_funnies.posts.models import Post


class BasePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'image_url', 'content']


class CreatePostForm(BasePostForm):
    pass


class EditPostForm(BasePostForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image_url'].help_text = ''


class DeletePostForm(ReadonlyViewMixin, BasePostForm):
    read_only_fields = ['title', 'image_url', 'content']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image_url'].help_text = ''
