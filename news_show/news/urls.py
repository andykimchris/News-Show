from django.urls import path

from . import views

urlpatterns = [
    path('sources/', views.sources, name="sources"),
    path('articles/', views.articles, name="articles")
]