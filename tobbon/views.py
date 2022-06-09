import io
from django.shortcuts import render
from django.http import FileResponse

# Create your views here.

def index(request):
    context = dict()
    return render(request, 'index.html', context)

def wsdl(request):
    return FileResponse(open('wsdlOntoloji.wsdl','rb'))