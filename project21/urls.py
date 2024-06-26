from django.urls import path, include
from django.contrib import admin
from django.conf import settings # new
from  django.conf.urls.static import static #new


urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('main_info.urls')),
    path('business/', include('businesses.urls')),
    path('product/', include('prods_servs.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_URL)