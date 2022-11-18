from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('НЕ СТЫДНО ПОКАЗАТЬ')

def group_posts(request, slug):
    return HttpResponse('ДОБРО ПОЖАЛОВАТЬ, ЗАРУБЕЖНАЯ ДЕЛЕГАЦИЯ')