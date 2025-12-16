# urls.py
from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
# from rest_framework.documentation import include_docs_urls  # این خط رو حذف کنید چون لازم نیست  # noqa: F401
# from rest_framework_spectacular.views import SpectacularAPIView, SpectacularSwaggerView , SpectacularRedocView #, SpectacularRedocView # اگر میخواهید از Redoc استفاده کنید، این را هم uncomment کنید
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView , SpectacularRedocView  #, SpectacularRedocView # اگر میخواهید از Redoc استفاده کنید، این را هم uncomment کنید



urlpatterns = [
    path('admin/', admin.site.urls),
    
    # برای استفاده از browsable API:
    path('api-auth/', include('rest_framework.urls')),
    
    # path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include("accounts.urls")),  # فرض بر این است که urls.py در accounts/ وجود دارد
    path('blog/', include('blog.urls')),
        
   # مسیرهای مربوط به drf-spectacular
    # path('api-core/', include('include_docs_urls')),  # فرض بر این است که urls.py در blog/api/v1/ وجود دارد
    path('schema/', SpectacularAPIView.as_view(), name='schema'), # این مسیر schema را فراهم می‌کند
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'), # این مسیر Swagger UI را نمایش می‌دهد
    # اگر می‌خواهید از Redoc هم استفاده کنید:
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

#serving static files and media files for development

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# Swagger UI: http://127.0.0.1:8000/swagger/#/

