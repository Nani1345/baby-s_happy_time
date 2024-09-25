from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Activity


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

def my_activity_index(request):
  activities = request.user.activities.all()
  return render(request, 'activities/my_activities_index.html', { 'activities': activities })

def add_my_activities(request, activity_id):
  activity = Activity.objects.get(id=activity_id)
  request.user.activities.add(activity)
  return redirect('activity-index')

class ActivityCreate(CreateView):
  model = Activity
  # fields = ['age', 'name', 'time', 'location', 'description']
  fields = '__all__'

class ActivityUpdate(UpdateView):
  model = Activity
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['time', 'location', 'description']

class ActivityDelete(DeleteView):
  model = Activity
  success_url = '/activities/'