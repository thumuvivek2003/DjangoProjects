import requests
from bs4 import BeautifulSoup
from django.utils import timezone
from datetime import datetime
import logging
from .models import NewsArticle, NewsSource, Category

logger = logging.getLogger(__name__)

class NewsScraper:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
    
    def scrape_bbc_news(self):
        """Scrape BBC News"""
        try:
            url = "https://www.bbc.com/news"
            response = self.session.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Get or create BBC source
            source, created = NewsSource.objects.get_or_create(
                name="BBC News",
                defaults={'url': url}
            )
            
            # Find article links
            articles = soup.find_all('a', {'data-testid': 'internal-link'})
            
            for article in articles[:10]:  # Limit to 10 articles
                try:
                    article_url = article.get('href')
                    if not article_url.startswith('http'):
                        article_url = f"https://www.bbc.com{article_url}"
                    
                    title_elem = article.find('h2') or article.find('h3')
                    if not title_elem:
                        continue
                    
                    title = title_elem.get_text().strip()
                    
                    # Skip if article already exists
                    if NewsArticle.objects.filter(title=title, source=source).exists():
                        continue
                    
                    # Get article content
                    article_response = self.session.get(article_url)
                    article_soup = BeautifulSoup(article_response.content, 'html.parser')
                    
                    # Extract content
                    content_div = article_soup.find('div', {'data-component': 'text-block'})
                    content = content_div.get_text().strip() if content_div else "Content not available"
                    
                    # Extract image
                    img_tag = article_soup.find('img')
                    image_url = img_tag.get('src') if img_tag else ""
                    
                    # Create article
                    NewsArticle.objects.create(
                        title=title,
                        content=content,
                        url=article_url,
                        source=source,
                        image_url=image_url,
                        published_at=timezone.now(),
                        summary=content[:200] + "..." if len(content) > 200 else content
                    )
                    
                except Exception as e:
                    logger.error(f"Error scraping article: {e}")
                    continue
                    
        except Exception as e:
            logger.error(f"Error scraping BBC News: {e}")
    
    def scrape_reddit_news(self):
        """Scrape Reddit News"""
        try:
            url = "https://www.reddit.com/r/news/"
            response = self.session.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Get or create Reddit source
            source, created = NewsSource.objects.get_or_create(
                name="Reddit News",
                defaults={'url': url}
            )
            
            # Find posts
            posts = soup.find_all('h3')
            
            for post in posts[:10]:
                try:
                    link = post.find('a')
                    if not link:
                        continue
                    
                    title = link.get_text().strip()
                    post_url = link.get('href')
                    
                    if not post_url.startswith('http'):
                        post_url = f"https://www.reddit.com{post_url}"
                    
                    # Skip if article already exists
                    if NewsArticle.objects.filter(title=title, source=source).exists():
                        continue
                    
                    NewsArticle.objects.create(
                        title=title,
                        content="Reddit post - click to view full content",
                        url=post_url,
                        source=source,
                        published_at=timezone.now(),
                        summary=title
                    )
                    
                except Exception as e:
                    logger.error(f"Error scraping Reddit post: {e}")
                    continue
                    
        except Exception as e:
            logger.error(f"Error scraping Reddit: {e}")
    
    def scrape_all_sources(self):
        """Scrape all active sources"""
        self.scrape_bbc_news()
        self.scrape_reddit_news()
        logger.info("Scraping completed for all sources")