from django.urls import path
from . import views

urlpatterns = [
	path('p', views.insert, name='tasks_post'),
	# path('g', views.get, name='tasks_get'),
]
