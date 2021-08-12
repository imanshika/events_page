from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("create_event", views.create_event, name = "create_event"),
    path("update/<int:id>/", views.update, name='update'),
]
