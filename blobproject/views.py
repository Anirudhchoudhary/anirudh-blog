from django.views.generic import TemplateView
from django.shortcuts import render
import blog.models

class Home(TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, *args, **kwargs):
        """
        Add custom context data for index page. 
        """

        featured_list = blog.models.Post.postobject.select_related("images").order_by("-created_at")[:3]
        recent_list = blog.models.Post.postobject.select_related("images").order_by("-created_at")[:10]
        news = blog.models.Post.newsobject.select_related("images").order_by("-created_at")[:10]
        context = super(Home, self).get_context_data(*args , **kwargs)
        context.update({"featured_list": featured_list,
                        "recent_list": recent_list,
                        "news_list": news})

        return context


def error_404(request, exception):
    return render(request, "404.html", {})

def error_500(request, exception=None):
    return render(request, "500.html", {})

def error_403(request, exception=None):
    return render(request, "403.html", {})

def error_400(request, exception=None):
    return render(request, "400.html", {})
