from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
urlpatterns = [
    
    path('profile/', views.profile, name = 'blog-profile'),
    path('setting/', views.setting, name = 'blog-setting'),

]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)