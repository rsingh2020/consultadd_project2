from django.urls import path
from . import views

urlpatterns = [
    path("", views.BLOG_POSTS_index, name="BLOG_POSTS_index"),
    path("<int:pk>/", views.BLOG_POSTS_detail, name="BLOG_POSTS_detail"),
    path("<category>/", views.BLOG_POSTS_category, name="BLOG_POSTS_category"),
]