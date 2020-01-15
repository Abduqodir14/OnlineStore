from django.urls import path
from landing.views import home, landing

app_name = 'landing'
urlpatterns = [
    path('', landing, name='landing'),
]