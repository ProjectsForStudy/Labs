from django.urls import path
from . import views

urlpatterns = [
    # Главная страница - список всех статей
    path('', views.archive, name='archive'),

    # Страница отдельной статьи
    path('article/<int:article_id>/', views.get_article, name='get_article'),
]




