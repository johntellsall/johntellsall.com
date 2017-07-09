from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from .models import Cat


def index(request):
    cats = Cat.objects.all()
    context = {'cats': cats}
    return render(request, 'cats/list.html', context)

@login_required
def hidden(request):
	context = {}
	return render(request, 'cats/hello.html', context)