from django.shortcuts import render
from django.http import HttpResponse

from .models import Cat


def index(request):
    cats = Cat.objects.all()
    output = ', '.join([cat.name for cat in cats])
    return HttpResponse(output)