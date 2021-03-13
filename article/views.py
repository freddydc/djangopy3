from django.shortcuts import render
from .models import *
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)

# Create your views here.


class ArticleListView(ListView):
    ### Notas:
        ## Name, "queryset" is default.
        ## Name, "template_name" is default.

    template_name = 'my_articles/my_article_list.html'
    queryset = Article.objects.all()


class ArticleDetailView(DetailView):
    template_name = 'my_articles/my_article_details.html'
    queryset = Article.objects.all()