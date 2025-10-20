from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('simple/', views.simple_view, name='simple_view'),
    path('<int:item_id>/', views.detail, name='detail'),
]