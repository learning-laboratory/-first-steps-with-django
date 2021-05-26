from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)

from .forms import ArticleModelForm
from .models import Article

class ArticleCreateView(CreateView):
    template_name = "articles/article_create.html"
    form_class = ArticleModelForm
    queryset = Article.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class ArticleUpdateView(UpdateView):
    template_name = 'articles/article_update.html'
    form_class = ArticleModelForm
    queryset = Article.objects.all()

    def get_object(self):
        return get_object_or_404(Article, id=self.kwargs.get("id"))

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class ArticleListView(ListView):
    template_name = "articles/article_list.html"
    queryset = Article.objects.all()

class ArticleDetailView(DetailView):
    template_name = "articles/article_detail.html"

    def get_object(self):
        return get_object_or_404(Article, id=self.kwargs.get("id"))

class ArticleDeleteView(DeleteView):
    template_name = "articles/article_delete.html"
    #success_url = "/blog/"

    def get_object(self):
        return get_object_or_404(Article, id=self.kwargs.get("id"))
    
    def get_success_url(self):
        return reverse("articles:article_list")