from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):

    # лог выыодится  одновремеено в консоль и файл
    return HttpResponse("""home Work 2 """)