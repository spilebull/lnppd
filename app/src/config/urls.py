# ==================================================
# URL Configuration
# ==================================================
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('main.python.urls')),
    path('admin/', admin.site.urls),
]
