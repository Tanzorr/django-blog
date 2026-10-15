from django.views.generic import DetailView, ListView

from blog.models import Post


class PostListView(ListView):
    queryset = Post.objects.published().select_related("author")


class PostDetailView(DetailView):
    queryset = Post.objects.published().select_related("author")
