from django.urls import path
from posts.views import PostDetailView, PostListView

urlpatterns = [
    path('<int:pk>/', PostDetailView.as_view()),
    path('', PostListView.as_view()),
]