from django.urls import path
from .views import Noun_project

urlpatterns = [
    path('<str:item>/', Noun_project.as_view(), name='noun_project')
]