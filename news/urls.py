from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.sources, name="sources"),
    url(r'^news/articles/$', views.articles, name="articles"),

]
