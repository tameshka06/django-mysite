from django.urls import path
from . import views

urlpatterns = [
    # Посты
    path("posts/", views.post_list, name="post_list"),
    path("posts/<slug:slug>/", views.post_detail, name="post_detail"),
    # Блоги
    path("blogs/", views.blog_list, name="blog_list"),
    path("blogs/create/", views.create_blog, name="create_blog"),
]
