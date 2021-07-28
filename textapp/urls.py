from django.urls import path
from .views import index


# create your url paths here

urlpatterns = [
    path('', index, name='index')
]
