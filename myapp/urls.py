from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('simple/', views.simple_view, name='simple_view'),
    path('<int:item_id>/', views.detail, name='detail'),
    path('create/', views.create_item, name='create_item'),
    path('<int:item_id>/edit/', views.edit_item, name='edit_item'),
    path('<int:item_id>/delete/', views.delete_item, name='delete_item'),
]