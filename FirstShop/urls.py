from django.contrib import admin
from django.urls import path, include
from landing import urls as landing_urls
from landing.views import home
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('landing/', include(landing_urls, namespace='landing')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
