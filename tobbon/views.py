import io
from django.shortcuts import render
from django.http import FileResponse
from django.urls import reverse

# Create your views here.

def index(request):
    context = dict()
    return render(request, 'index.html', context)

def absolute_url(self):
    return reverse('api/belgeler', kwargs={'slug':self.slug})