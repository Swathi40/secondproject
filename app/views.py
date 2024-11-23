from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def saiganesh(request):
    return HttpResponse('haii saiganesh')

def seemakurthi(request):
    return HttpResponse(' <h1>Hello swathi</h1>')


def Django(request):
    return HttpResponse('<i><marcquee><hello welcome my django first project</marcquee></i>')