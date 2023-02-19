from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='tasks'),
	path('p', views.insert, name='task_insert'),
	path('d', views.delete, name='task_delete'),
	# path('g', views.get, name='tasks_get'),
]
