from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Anounce
from django.http import JsonResponse
import json

# Create your views here.

def index(request):
	return render(request, 'index.html', {})

def anounce(request):
	return render(request, 'anounce/anounce.html',{})

@csrf_exempt
def get_list(request):
	anounce_list = Anounce.objects.order_by('-created').values()
	return JsonResponse({"result":list(anounce_list)})

@csrf_exempt
def detail_list(request, num):
	return render(request, 'anounce/detail_list.html', {"num":num})

@csrf_exempt
def get_context(request, num):
	context = Anounce.objects.filter(id=num).values()
	return JsonResponse({"result":list(context)})

