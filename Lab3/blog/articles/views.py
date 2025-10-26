from django.shortcuts import render, get_object_or_404
from .models import Article

def archive(request):
    posts = Article.objects.all().order_by('-created_date')
    return render(request, 'archive.html', {'posts': posts})

def get_article(request, article_id):
    # Получение статьи по ID или возврат 404
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'article.html', {'post': article})