from django.urls import path

from cities.views import *

urlpatterns = [
    path('', home, name='home'),
    path('<int:pk>/', home, name='home'),

]
