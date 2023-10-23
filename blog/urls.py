from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.helloView),
    path('now_data/', views.now_dataView),
    path('goodby/', views.goodbyView),
    path('post/', views.postListView),
    path('post/', views.postListView),
    path('post_detail/<int:id>/', views.postDetailView),

]
