from django.urls import path
from .views import (
    ArticleListView,
    ArticleDetailView,
)

app_name = 'articles'

urlpatterns = [
    path('', ArticleListView.as_view(), name='article-list'),
    ## PK is required '<int:pk>/' for views based in class. PK <=> ID ##
    path('<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
]
