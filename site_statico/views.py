from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    # return HttpResponse(f" Meu Primeiro Site Feito Sozinho ")
    return render(request, 'site_statico/home.html')
