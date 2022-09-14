from django.shortcuts import render
from django.core import serializers
from .models import *
from django.http import JsonResponse
# Create your views here.

def getSpeaker(request):
    #serialze the data from the model speakers
    data = serializers.serialize('json', Speaker.objects.all())
    data={"speakers":data}
    res=JsonResponse(data)
    return res

