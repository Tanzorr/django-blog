from django.urls import path

from blog import views

app_name = "blog"

urlpatterns = [
    path("", views.PostListView.as_view(), name="post_list"),
    path("posts/<slug:slug>/", views.PostDetailView.as_view(), name="post_detail"),
]
