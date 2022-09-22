from django.shortcuts import render ,redirect
from django.http import HttpResponse ,JsonResponse
import requests
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def home(request):
    return HttpResponse ("hello")