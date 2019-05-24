from django.urls import path
from .views import FileListView, FileDetailView, FileCreateView, FileUpdateView, FileDeleteView
from . import views

urlpatterns = [
    path('', FileListView.as_view(), name='index'),
    path('file/<int:pk>/', FileDetailView.as_view(), name='file-detail'),
    path('file/new/', FileCreateView.as_view(), name='file-create'),
    path('file/<int:pk>/update/', FileUpdateView.as_view(), name='file-update'),
    path('file/<int:pk>/delete/', FileDeleteView.as_view(), name='file-delete'),
    path('home/', views.home, name='blog-home'),
    path('profile/', views.porfile, name='blog-profile'),
]