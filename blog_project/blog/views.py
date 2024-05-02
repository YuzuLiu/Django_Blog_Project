from django.shortcuts import render, get_object_or_404
from django.views import generic

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

class BlogListView(generic.ListView):
    model = Blog
    context_object_name = 'blog_list'
    paginate_by = 5

class BlogDetailView(generic.DetailView):
    model = Blog

    def blog_detail_view(request, primary_key):
        blog = get_object_or_404(Blog, pk=primary_key)
        return render(request, 'catalog/blog_detail.html', context={'blog': blog})

class BloggerListView(generic.ListView):
    model = Blogger
    context_object_name = 'blogger_list'
    paginate_by = 5

class BloggerDetailView(generic.DetailView):
    model = Blogger

    def blogger_detail_view(request, primary_key):
        blog = get_object_or_404(Blogger, pk=primary_key)
        return render(request, 'catalog/blogger_detail.html', context={'blogger': blogger})
