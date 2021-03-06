from django.urls import path
from .views import nippoDetailView, nippoListView, nippoCreateView

urlpatterns = [
    path("", nippoListView, name='nippo_list'),
    path("detail/<int:pk>/", nippoDetailView, name='detail'),
    path("create/", nippoCreateView, name='create'),
]