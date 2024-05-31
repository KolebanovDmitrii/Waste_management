from django.urls import path
from .views import home

urlpatterns = [
    path('', home, name='home'),
]
# locations/urls.py
from django.urls import path
from .views import waste_disposal_location_list

urlpatterns = [
    path('', waste_disposal_location_list, name='waste_disposal_location_list'),
]
