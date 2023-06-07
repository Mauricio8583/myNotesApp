from django.urls import path
from . import views

# Creating the URLs for the views

urlpatterns = [
    path('', views.getRoutes, name="routes"),
    path('notes/', views.getNotes, name="notes"),
    path('notes/<str:pk>', views.getNote, name="note")
]