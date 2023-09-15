from django.contrib import admin
from django.urls import path, include 
from django.conf.urls.static import static
from django.conf import settings 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.site.site_title = 'Kivu Service Consulting Website'
admin.site.site_header = 'Kivu Consulting Service Administration'
admin.site.index_title = 'KSC admin'

urlpatterns = [
    path('admin/', admin.site.urls),  
    path('', include('website.urls')),   
    # =path('', include('user.urls') ), 
    # path('api/kns/', include('djoser.urls')), 
    # path("api/kns/", include('djoser.urls.authtoken')),
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
