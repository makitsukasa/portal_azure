from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='calendarapp'),
	path('2', views.hidden, name='calendarapp'),
	path('p', views.insert, name='event_insert'),
	# path('d', views.delete, name='event_delete'),
]
