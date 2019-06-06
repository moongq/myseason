from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('article.urls')),
    path('tinymce/', include('tinymce.urls')),
]
