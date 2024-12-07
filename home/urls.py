from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home/', views.home, name='home'),
    path('cart/', views.cart, name='cart'),
   
]

# Add static media URL patterns
if settings.DEBUG:  # Serve media files only in debug mode
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
