from django.shortcuts import render
from django.views import generic

from .models import Blog, Blogger, Type

# Create your views here.
def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_blogs = Blog.objects.all().count()

    # The 'all()' is implied by default.
    num_bloggers = Blogger.objects.count()

    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_blogs': num_blogs,
        'num_bloggers': num_bloggers,
        'num_visits': num_visits,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

class BlogListView(generic.ListView):
    model = Blog
    context_object_name = 'blog_list'
    paginate_by = 5

class BlogDetailView(generic.DetailView):
    model = Blog

class BloggerListView(generic.ListView):
    model = Blogger
    context_object_name = 'blogger_list'
    paginate_by = 5

class BloggerDetailView(generic.DetailView):
    model = Blogger
