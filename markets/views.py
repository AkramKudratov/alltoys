from django.http import HttpResponse
from django.shortcuts import render


def markets(request):
    return HttpResponse('Welcome to markets')
