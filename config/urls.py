from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('index.urls')),
    path('vet/', include('vet.urls')),
    path('delivred/', include('delivered.urls')),
    
    re_path(r"media/(.*)", serve, {"document_root": settings.MEDIA_ROOT}),
]
