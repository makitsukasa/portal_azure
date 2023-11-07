from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='calendarapp'),
	path('2', views.hidden, name='calendarapp'),
	path('c', views.create, name='event_create'),
	path('u', views.update, name='event_update'),
	path('d', views.delete, name='event_delete'),
]
