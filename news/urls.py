from django.urls import path

from . import views

urlpatterns = [
    path('', views.sources, name="sources"),
    path('news/articles/$', views.articles, name="articles"),

]
