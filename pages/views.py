from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
from django.conf import settings
def home_view(request):     
    return render(request, 'pages/home_page.html', {'debug': settings.DEBUG})



