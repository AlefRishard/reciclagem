
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("home.urls")),
    path("usuario/", include("usuario.urls")),
    path('mapa/', include("mapa.urls")),
    path('ponto/', include('ponto.urls')),
]
