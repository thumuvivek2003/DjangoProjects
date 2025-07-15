import requests
from bs4 import BeautifulSoup
from .models import News
from celery import shared_task

def scrape_bbc_news():
    url = 'https://www.bbc.com/news'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    cards = soup.find_all('div', attrs={'data-testid': 'dundee-card'})[:5]  

    for card in cards:

        link_tag = card.find('a', attrs={'data-testid': 'internal-link'})
        if not link_tag:
            continue  

        relative_url = link_tag.get('href', '')
        full_link = 'https://www.bbc.com' + relative_url

        title_tag = card.find('h2', attrs={'data-testid': 'card-headline'})
        if not title_tag:
            continue

        title = title_tag.text.strip()

        print(f"Title: {title}")
        print(f"Link: {full_link}\n")

        News.objects.get_or_create(title=title, link=full_link)

