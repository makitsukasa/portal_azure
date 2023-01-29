from django.urls import path
from . import views

urlpatterns = [
	path('p', views.post, name='twitter_post'),
	path('g', views.get, name='twitter_get'),
]
