from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'GCacc/teste.html')

def index(request):
    return HttpResponse("Teste do index")
