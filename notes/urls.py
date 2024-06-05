
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('notes/', views.note_list, name='note_list'),
    path('notes/<int:pk>/', views.note_detail, name='note_detail'),
    path('notes/new/', views.note_create, name='note_create'),
    path('notes/<int:pk>/edit/', views.note_edit, name='note_edit'),
    path('notes/<int:pk>/delete/', views.note_delete, name='note_delete'),
     path('posts/', views.post_list, name='post_list'),
    path('posts/<int:pk>/', views.post_detail, name='post_detail'),
    path('posts/new/', views.post_create, name='post_create'),
    path('posts/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('posts/<int:pk>/delete/', views.post_delete, name='post_delete'),
]
