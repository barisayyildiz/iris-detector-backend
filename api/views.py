from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .util import *

# Create your views here.
@api_view(['GET', 'POST'])
def hello_world(request):
	if request.method == 'GET':
		pass
	elif request.method == 'POST':
		return Response(data={"result":predict(request.data)})
