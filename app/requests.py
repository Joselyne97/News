from app import app
import urllib.request,json
from .models import news

News = news.News


# Getting api key
api_key = app.config['NEWS_API_KEY']
sources_url = app.config["NEWS_API_SOURCES_URL"]

def get_news(category):
    '''e
    Function that gets the json response to our url request
    '''
    get_news_url = sources_url.format(category,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_sources = None

        if get_news_response['sources']:
            news_sources_list = get_news_response['sources']
            news_sources = process_sources(news_sources_list)


    return news_sources