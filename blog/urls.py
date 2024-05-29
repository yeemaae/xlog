from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name="Home"),
    path('post/<slug:post>/', views.single_post, name="single_post"),
    path('tag/<slug:tag>/', views.TagListView.as_view(), name="tag_post"),
]
