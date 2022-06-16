from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import UpdateView

from .models import Post
from .models import POST_NEWS
from .models import POST_POST


class PostListView(ListView):
    """Представление для отображения списка записей Post."""
    model = Post
    template_name = "post/post_list.html"
    paginate_by = 2
    ordering = ["-created_at",]

    def get_queryset(self):
        """Переопределяет стандартную выборку."""
        qs = super().get_queryset()
        return qs.filter(post_type=POST_NEWS)


class PostDetailView(DetailView):
    """Представление для отображения детальной информации о записи Post."""
    model = Post
    template_name = "post/post_detail.html"


class PostCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """Предсталвение для создания записи Post."""
    model = Post
    fields = [
        "author",
        "categories",
        "title",
        "text",
    ]
    template_name = "post/post_create.html"
    success_url = "/news/"
    permission_required = ("post.add_post",)

    def form_valid(self, form):
        form.instance.post_type = POST_NEWS
        return super().form_valid(form)


class PostDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """Представление для удаления записи Post."""
    model = Post
    template_name = "post/post_delete.html"
    success_url = "/news/"
    permission_required = ("post.delete_post",)


class PostUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    """Предсталвение для редиктирования данных в записи Post."""
    model = Post
    fields = ["title", "text"]
    template_name = "post/post_update.html"
    success_url = "/news/"
    permission_required = ("post.change_post",)


class ArticleCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """Представление для создания Статьи."""
    model = Post
    fields = [
        "author",
        "categories",
        "title",
        "text",
    ]
    template_name = "post/post_create.html"
    success_url = "/news/"
    permission_required = ("post.add_post",)

    def form_valid(self, form):
        form.instace.post_type = POST_POST
        return super().form_valid(form)


class ArticleUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    """Представление для редактирования Статьи."""
    model = Post
    fields = ["title", "text"]
    template_name = "post/post_update.html"
    success_url = "/news/"
    permission_required = ("post.change_post",)


class ArticleDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """Представление для удаления Статьи."""
    model = Post
    template_name = "post/post_delete.html"
    success_url = "/news/"
    permission_required = ("post.delete_post",)
