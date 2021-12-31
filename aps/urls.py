from django.urls import path 
from aps.views import *

app_name="aps"
urlpatterns = [
    path('list/', APSS.as_view(), name="list"),
    path('create/', CreateAPS.as_view(), name="create"),
]