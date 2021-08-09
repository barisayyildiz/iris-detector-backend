from django.urls import path
from .views import *


urlpatterns = [
	path('flower/', get_flower_name, name='hello')
]
