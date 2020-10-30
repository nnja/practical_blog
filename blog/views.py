from django.views.generic import DetailView, ListView

from blog.models import Post


class PostListView(ListView):
    model = Post
    queryset = Post.objects.filter(is_draft=False)


class PostDetailView(DetailView):
    model = Post
    queryset = Post.objects.filter(is_draft=False)
