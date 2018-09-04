from django.conf.urls import url
from . import views

urlpatterns = [
    url('sources/', views.sources, name="sources"),
    url('articles/', views.articles, name="articles"),

]
