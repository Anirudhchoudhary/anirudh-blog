from django.views.generic import TemplateView
import blog.models

class Home(TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, *args, **kwargs):
        """
        Add custom context data for index page. 

        """

        featured_list = blog.models.Post.objects.filter(is_active=True).select_related("images")[:3]
        recent_list = blog.models.Post.objects.filter(is_active=True).select_related("images").order_by("-created_at")
        context = super(Home, self).get_context_data(*args , **kwargs)
        context.update({"featured_list": featured_list, 
                        "recent_list": recent_list})
        return context
