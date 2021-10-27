from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse

def home_view(request):     
    return render(request, 'pages/home_page.html')



