from unicodedata import name
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<slug>', views.article_detail, name='article_detail'),
    path('article_create/', views.article_create, name='article_create'),
    path('<slug>/edit', views.edit_article, name="article_edit"),
    path('<slug>/delete', views.delete_article, name="article_delete"),
    path('<slug>/like', views.like_article, name="like_article"),
    path('<slug>/dislike', views.dislike_article, name="dislike_article"),
    path('<slug>/comment/<pk>/delete', views.delete_comment, name="delete_comment"),
    path('<slug>/comment/<pk>/edit', views.edit_comment, name="edit_comment"),
]