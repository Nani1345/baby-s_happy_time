from django.db import models
from datetime import date
from django.urls import reverse
from django.contrib.auth.models import User


AGE = (
  ('1', '0-1.5'),
  ('2', '1.5-3'),
  ('3', '3-5'),
  ('4', '5-7'),
  ('5', '7-10')
)
# Create your models here.
class Activity(models.Model):
  age = models.CharField(
    max_length=1,
    choices=AGE,
    default=AGE[0][0]
  )
  name = models.CharField(max_length=100)
  time = models.DateField('Activity Date')
  location = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  users = models.ManyToManyField(User, related_name='activities')
  
  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('activity-detail', kwargs={'activity_id': self.id})