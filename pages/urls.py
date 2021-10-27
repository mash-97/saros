from django.urls import path
from django.urls.resolvers import URLPattern 
from pages.views import *

urlpatterns = [ 
    path('', home_view, name='home'),
]