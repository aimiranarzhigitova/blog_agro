from django.urls import path
from blog import views

urlpatterns = [
    path('api/v1/posts/create/', views.PostCreateView.as_view()),
    path('api/v1/posts/', views.PostListView.as_view()),
    path('api/v1/posts/<int:pk>/', views.PostDetailView.as_view()),
    path('api/v1/posts/<int:pk>/update/', views.PostUpdateView.as_view()),
    path('api/v1/posts/<int:pk>/delete/', views.PostDeleteView.as_view()),
    path('api/v1/categories/', views.CategoryListCreateView.as_view()),
    path('api/v1/comments/', views.CommentListCreateView.as_view()),
    path('api/v1/comments/<int:pk>/', views.CommentDetailView.as_view()),
]