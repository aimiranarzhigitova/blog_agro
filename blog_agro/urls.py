from django.contrib import admin
from django.urls import path, include
from .swagger import urlpatterns as docurlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Post/', include('blog.urls')),
    path('User/', include('agro_user.urls')),
]


urlpatterns += docurlpatterns