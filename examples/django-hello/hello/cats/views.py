from django.shortcuts import render
from django.http import HttpResponse

from .models import Cat


def index(request):
    cats = Cat.objects.all()
    context = {'cats': cats}
    return render(request, 'cats/list.html', context)
