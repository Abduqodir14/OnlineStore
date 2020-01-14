from django.contrib import admin
from django.urls import path, include
from landing import urls as landing_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('landing/', include(landing_urls, namespace='landing'))
]
