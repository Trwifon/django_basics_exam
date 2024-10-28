from furry_funnies.author.models import Author

def get_profile_object():
    return Author.objects.first()