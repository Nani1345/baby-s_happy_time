from django.shortcuts import render
from django.http import HttpResponse



class Activity:  # Note that parens are optional if not inheriting from another class
  def __init__(self, age, name, time, location, description):
    self.age = age
    self.name = name
    self.time = time
    self.location = location
    self.description = description

activities = [
  Activity('1.5-3', 'Story time', '9/24/2024', 'downtown park', 'funny'),
  Activity('0-1.5', 'play time', '9/26/2024','community center', 'funny'),
]

# Create your views here.
def home(request):
  return HttpResponse('<h1>Hello ᓚᘏᗢ</h1>')

def about(request):
  return render(request, 'about.html')

def activity_index(request):
  return render(request, 'activities/index.html', { 'activities': activities })