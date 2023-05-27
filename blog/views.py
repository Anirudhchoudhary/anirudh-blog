import blog.models as models

from django.shortcuts import render
from django.db.models import Q

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


class Search(ListView):
    model = models.Post
    template_name = "post/search_result.html"
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = models.Post.objects.filter(
            Q(title__icontains=query)
        )

        return object_list