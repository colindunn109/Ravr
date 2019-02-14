from django.contrib import admin
from django.urls import path,include
from . import views

app_name = "posts"

urlpatterns = [
    path('postlist/',views.PostListView.as_view(),name="postlist"),
    path('postform/',views.PostCreateView.as_view(),name="create"),
    path('postlist/<pk>',views.PostDetailView.as_view(),name="postdetail")
]
