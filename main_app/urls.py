from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('activities/', views.activity_index, name='activity-index'),
  path('activities/<int:activity_id>/', views.activity_detail, name='activity-detail'),
]