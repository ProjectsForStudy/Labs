from django.urls import path, re_path
from . import views

urlpatterns = [
    # Главная страница - список всех статей
    path('', views.archive, name='archive'),
    # Страница отдельной статьи
    re_path(r'^article/(?P<article_id>\d+)/$', views.get_article, name='get_article'),
]

