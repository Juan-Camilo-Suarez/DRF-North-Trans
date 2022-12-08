from django.http import JsonResponse
from django.shortcuts import render


# Create your views here.

def main_api(request):
    return JsonResponse({
        'status': 'ok'
    })

#comment