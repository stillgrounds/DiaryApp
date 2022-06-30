from django.http import admin
from django.http import HttpResponse

def index(request):
    name = 'Efe Isibor'
    return HttpResponse(name)