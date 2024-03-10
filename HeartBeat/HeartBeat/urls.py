
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.ProfileManagementApp.urls')),
    path('api/', include('apps.AccountManagementApp.urls')),
    path('api/', include('apps.EstimationApp.urls')),
    path('api/', include('apps.TagManagmentApp.urls')),
]

