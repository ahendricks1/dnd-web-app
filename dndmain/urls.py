from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name = 'index'),
	path('<int:character_id>/detail/', views.detail, name = 'detail'),
	path('<int:party_id>/party/', views.party, name = 'party'),
]