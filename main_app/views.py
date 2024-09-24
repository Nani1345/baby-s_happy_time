from django.shortcuts import render
from .models import Activity



# class Activity:  # Note that parens are optional if not inheriting from another class
#   def __init__(self, age, name, time, location, description):
#     self.age = age
#     self.name = name
#     self.time = time
#     self.location = location
#     self.description = description

# activities = [
#   Activity(age='1.5-3',name='Story time', time='9/24/2024', location='downtown park', description='funny'),
#   Activity('0-1.5', 'play time', '9/26/2024','community center', 'funny'),
# ]

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def activity_index(request):
  activities = Activity.objects.all()
  return render(request, 'activities/index.html', { 'activities': activities })

def activity_detail(request, activity_id):
  activity = Activity.objects.get(id=activity_id)
  return render(request, 'activities/detail.html', { 'activity': activity})