from django import template
from furry_funnies.common.helpers import get_profile_object


register = template.Library()

@register.simple_tag
def get_user():
    return get_profile_object()