import blog.models as models

from django.shortcuts import render

from django.views.generic import ListView, DetailView
# Create your views here.


class PostListView(ListView):
    model = models.Post
    queryset = models.Post.objects.all().select_related("images")
    template_name = "post/post_list.html"
    paginate_by = 20

class FeaturedListView(ListView):
    model = models.Post
    queryset = models.Post.objects.filter(is_active=True).select_related("images")[:3]
    template_name= "post/featured_blog.html"

class RecentListView(ListView):
    model = models.Post
    queryset = models.Post.objects.filter(is_active=True).select_related("images").order_by("-created_at")
    template_name = "post/recent_post_list.html"
    paginate_by = 10

class PostDetails(DetailView):
    model = models.Post
    slug_field = "pk"
    queryset = models.Post.objects.filter(is_active=True).select_related("images")
    template_name = "post/post_details.html"
    