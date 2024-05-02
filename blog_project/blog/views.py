from django.shortcuts import render

from .models import Blog, Blogger, Type

# Create your views here.
def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_blogs = Blog.objects.all().count()

    # The 'all()' is implied by default.
    num_bloggers = Blogger.objects.count()

    context = {
        'num_blogs': num_blogs,
        'num_bloggers': num_bloggers,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
