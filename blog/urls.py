from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello_view),
    path('now_data/', views.now_data_view),
    path('goodby/', views.goodby_view),
    path('post/', views.post_list_view),
    path('post_detail/<int:id>/', views.post_detail_view),

]
