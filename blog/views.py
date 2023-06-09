from typing import Any
import blog.models as models

from django.shortcuts import render
from django.http.response import HttpResponse
from django.db.models import Q, F
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt    
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

    def render_to_response(self, context, **response_kwargs) -> HttpResponse:
        pk = self.get_object().pk
        models.PostStats.objects.filter(post__pk=pk).update(viewed = F('viewed') + 1)
        return super(PostDetails, self).render_to_response(context, **response_kwargs)


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

@csrf_exempt
def like_post(request, pk):
    """
    function to accept like comment. 
    """

    try:
        if request.method == "POST":
            post_stat = models.PostStats.objects.filter(post__pk=pk).first()
            
            if post_stat:
                post_stat.like += 1
                post_stat.save() 
            else:
                post = models.Post.objects.filter(pk=pk).first()
                models.PostStats.objects.create(
                    like=1,
                    post_id=post.id
                )

            return JsonResponse(data={
                "msg": "Updated like message",
                "status": 200
            })
        else: 
            return JsonResponse(data={
                "msg": "Only Post method allowed",
                "status": 405
            })
    except Exception as e:
        return JsonResponse(data={
            "msg": str(e),
            "status": 400
        })



