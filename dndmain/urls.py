from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name = 'index'),
	path('<int:party_id>/', views.detail, name = 'detail'),
	path('<int:party_id>/party/', views.party, name = 'party'),
]