from django.shortcuts import render
from django.http import Http404
from .models import Article

def archive(request):
    # Получение статьи, отсортированной по дате
    posts = Article.objects.all().order_by('-created_date')
    return render(request, 'archive.html', {'posts': posts})

def get_article(request, article_id):
    try:
        # Поиск статьи по ID
        post = Article.objects.get(id=article_id)
        # Передача найденной статьи в шаблон
        return render(request, 'article.html', {'post': post})
    except Article.DoesNotExist:
        # Если статья не найдена - возврашается ошибка 404
        raise Http404("Статья не найдена")