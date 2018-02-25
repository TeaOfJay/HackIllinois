from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('user_data/', include('user_data.urls')),
    path('admin/', admin.site.urls),
]
