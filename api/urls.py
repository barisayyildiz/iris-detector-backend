from django.urls import path
from .views import *


urlpatterns = [
	path('flower/', hello_world, name='hello')
]
