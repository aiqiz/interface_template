from django.urls import path
from .views import all_data

urlpatterns = [
    path('', all_data)
]
