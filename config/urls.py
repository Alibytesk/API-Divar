from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from config.settings import MEDIA_URL, MEDIA_ROOT, DEBUG
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView

urlpatterns = [
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(), name='swagger'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
]
if DEBUG:
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)