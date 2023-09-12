from django.urls import path
from . import views

urlpatterns = [
	path('n', views.post, name='misskey_note'),
	path('g', views.get, name='misskey_get'),
]
