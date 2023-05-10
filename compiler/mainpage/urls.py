from django.urls import path

from . import views

urlpatterns = [
    path('', views.mainpage, name='mainpage'),
    path('<int:file_id>/', views.view_file, name='view_file'),
    path('add_file/<int:folder_id>/', views.add_file, name='add_file'),
    path('add_folder/<int:folder_id>/', views.add_folder, name='add_folder'),
    path('remove_file/<int:file_id>/', views.remove_file, name='remove_file'),
    path('remove_folder/<int:folder_id>/', views.remove_folder, name='remove_folder'),
    path('download/<int:file_id>/', views.download, name='download'),
]