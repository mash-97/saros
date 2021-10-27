from django.urls import path
from django.urls.resolvers import URLPattern 

from users.views import *


app_name="users"
urlpatterns = [ 
    path('test/', test, name="test"),
    path('profile/<int:pk>', UserProfile.as_view(), name="profile"),
]