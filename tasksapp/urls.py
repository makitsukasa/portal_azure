from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='tasks'),
	path('p', views.insert, name='tasks_post'),
	# path('g', views.get, name='tasks_get'),
]
