from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from .models import NewsArticle, Category, NewsSource

def news_list(request):
    """Display list of news articles"""
    articles = NewsArticle.objects.filter(is_active=True)
    
    # Filter by category
    category_id = request.GET.get('category')
    if category_id:
        articles = articles.filter(category_id=category_id)
    
    # Filter by source
    source_id = request.GET.get('source')
    if source_id:
        articles = articles.filter(source_id=source_id)
    
    # Search functionality
    query = request.GET.get('q')
    if query:
        articles = articles.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )
    
    # Pagination
    paginator = Paginator(articles, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'articles': page_obj,
        'categories': Category.objects.all(),
        'sources': NewsSource.objects.filter(is_active=True),
        'current_category': category_id,
        'current_source': source_id,
        'query': query,
    }
    
    return render(request, 'news_aggregator/news_list.html', context)

def news_detail(request, pk):
    """Display single news article"""
    article = get_object_or_404(NewsArticle, pk=pk, is_active=True)
    
    # Get related articles
    related_articles = NewsArticle.objects.filter(
        source=article.source,
        is_active=True
    ).exclude(pk=pk)[:5]
    
    context = {
        'article': article,
        'related_articles': related_articles,
    }
    
    return render(request, 'news_aggregator/news_detail.html', context)

def trigger_scraping(request):
    """Manually trigger news scraping"""
    from .tasks import scrape_news
    
    if request.method == 'POST':
        scrape_news.delay()
        return render(request, 'news_aggregator/scraping_triggered.html')
    
    return render(request, 'news_aggregator/trigger_scraping.html')