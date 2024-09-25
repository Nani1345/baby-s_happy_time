from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('activities/', views.activity_index, name='activity-index'),
  path('activities/<int:activity_id>/', views.activity_detail, name='activity-detail'),
  path('activities/myactivities/', views.my_activity_index, name='my-activity-index'),
  path('activities/create/', views.ActivityCreate.as_view(), name='activity-create'),
  path('activities/<int:pk>/update/', views.ActivityUpdate.as_view(), name='activity-update'),
  path('activities/<int:pk>/delete/', views.ActivityDelete.as_view(), name='activity-delete'),
  path('add_activity/<int:activity_id>/', views.add_my_activities, name='add-my-activities'),
]