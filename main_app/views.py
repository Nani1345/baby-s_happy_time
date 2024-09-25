from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Activity
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden


# Create your views here.
class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

def activity_index(request):
  activities = Activity.objects.all()
  return render(request, 'activities/index.html', { 'activities': activities })

def activity_detail(request, activity_id):
  activity = Activity.objects.get(id=activity_id)
  return render(request, 'activities/detail.html', { 'activity': activity})

@login_required
def my_activity_index(request):
  activities = request.user.activities.all()
  return render(request, 'activities/my_activities_index.html', { 'activities': activities })

@login_required
def add_my_activities(request, activity_id):
  activity = Activity.objects.get(id=activity_id)
  request.user.activities.add(activity)
  return redirect('activity-index')

class ActivityCreate(LoginRequiredMixin, CreateView):
  model = Activity
  fields = ['age', 'name', 'time', 'location', 'description']

  def form_valid(self, form):
    # form.instance.user = self.request.user 
    form.instance.creator = self.request.user  
    return super().form_valid(form)

class ActivityUpdate(LoginRequiredMixin, UpdateView):
  model = Activity
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['time', 'location', 'description']

  def get_object(self, queryset=None):
        activity = super().get_object(queryset)
        if activity.creator != self.request.user:
            raise HttpResponseForbidden("You are not allowed to update this activity.")
        return activity

class ActivityDelete(LoginRequiredMixin, DeleteView):
  model = Activity
  success_url = '/activities/'

  def get_object(self, queryset=None):
        activity = super().get_object(queryset)
        if activity.creator != self.request.user:
            raise HttpResponseForbidden("You are not allowed to delete this activity.")
        return activity

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('activity-index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)
 