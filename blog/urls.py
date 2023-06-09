from django.urls import path

import blog.views as views

urlpatterns = [
    path("list/", views.PostListView.as_view(), name="post_list"),
    path("featured_list/", views.FeaturedListView.as_view(), name="post_featured_list"),
    path("recent/", views.RecentListView.as_view(), name="post_recent_view"),
    path("detail/<int:pk>", views.PostDetails.as_view(), name="blog_detail"),
    path("search_results/", views.Search.as_view(), name="search_results"),
    path('like/<int:pk>', views.like_post, name='like_post'),
]