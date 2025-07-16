from celery import shared_task
from .scraper import NewsScraper
import logging

logger = logging.getLogger(__name__)

@shared_task
def scrape_news():
    """Celery task to scrape news"""
    try:
        scraper = NewsScraper()
        scraper.scrape_all_sources()
        logger.info("News scraping task completed successfully")
        return "News scraping completed"
    except Exception as e:
        logger.error(f"Error in news scraping task: {e}")
        return f"Error: {e}"

@shared_task
def cleanup_old_articles():
    """Remove articles older than 30 days"""
    from django.utils import timezone
    from datetime import timedelta
    from .models import NewsArticle
    
    cutoff_date = timezone.now() - timedelta(days=30)
    deleted_count = NewsArticle.objects.filter(published_at__lt=cutoff_date).delete()[0]
    logger.info(f"Deleted {deleted_count} old articles")
    return f"Deleted {deleted_count} old articles"