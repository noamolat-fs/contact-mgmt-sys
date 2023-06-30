from django.urls import path

from . import views

app_name = "contacts"
urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("<int:uid>/", views.read, name="read"),
    path("<int:uid>/update/", views.update, name="update"),
    path("<int:uid>/", views.read, name="delete"),
]