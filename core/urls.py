from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('books.urls')),
    path('api/auth/', include('rest_framework.urls')),
    path('api/accounts', include('accounts.urls')),
    path("api/accounts/rest-auth/", include("rest_auth.urls")),
    path("api/accounts/registration/", include("rest_auth.registration.urls")),
]
