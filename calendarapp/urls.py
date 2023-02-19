from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='calendarapp'),
	path('2', views.hidden, name='calendarapp'),
]
