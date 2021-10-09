from django.urls import path
from django.urls.resolvers import URLPattern 

from user.views import *


app_name="user"
urlpatterns = [ 
    path('test/', test, name="test"),
]