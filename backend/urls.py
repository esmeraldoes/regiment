# project/urls.py

from django.contrib import admin
from django.urls import path, include
from rest_framework import urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bibleApp.urls')),
    path('accounts/', include('allauth.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('api-auth/', include(urls)),

]


