from django.contrib import admin
from django.urls import path, include # Импортируем функцию include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Подключение URL-адреса из приложения articles.
    # Любой URL, начинающийся с /, будет перенаправлен в articles.urls
    path('', include('articles.urls')),
]