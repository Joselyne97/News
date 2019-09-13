# from app import app
import urllib.request,json
from .models import News

# News = news.News


# Getting api key
api_key = None

# Getting sources url
sources_url = None

def configure_request(app):
    global api_key,sources_url
    api_key = app.config['NEWS_API_KEY']
    sources_url = app.config['NEWS_API_SOURCES_URL']
    print(api_key)
    print(sources_url)


def get_newss(category):
    '''
    Function that gets the json response to our url request
    '''
    get_newss_url = sources_url.format(category,api_key)

    with urllib.request.urlopen(get_newss_url) as url:
        get_newss_data = url.read()
        get_newss_response = json.loads(get_newss_data)

        news_sources = None

        if get_newss_response['sources']:
            news_sources_list = get_newss_response['sources']
            news_sources = process_sources(news_sources_list)


    return news_sources

def process_sources(news_list):
    '''
    Function  that processes the news sources and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain news details

    Returns :
        news_sources: A list of news objects
    '''
    news_sources = []
    for news_item in news_list:
        name = news_item.get('name')
        description = news_item.get('description')
        category = news_item.get('category')
        language = news_item.get('language')
        country = news_item.get('country')
        url = news_item.get('url')

        if description:
            news_object = News(name,description,category,language,country,url)
            news_sources.append(news_object)

    return news_sources