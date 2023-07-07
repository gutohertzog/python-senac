from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('inicio.urls')),
    path('nintendo/', include('nintendo.urls')),
    path('playstation/', include('playstation.urls')),
]

# adicionando as pastas das mídias nas ulrs do projeto
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

