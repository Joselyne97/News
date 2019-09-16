# from app import app
import urllib.request,json
from .models import News,Articles

# News = news.News


# Getting api key
api_key = None

# Getting sources url
sources_url = None
articles_url = None

def configure_request(app):
    global api_key,sources_url,articles_url
    api_key = app.config['NEWS_API_KEY']
    sources_url = app.config['NEWS_API_SOURCES_URL']
    articles_url = app.config['NEWS_API_ARTICLES_URL']


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

def get_articles(id):
    '''
    Function that processes the articles and returns a list of articles objects
    '''
    get_articles_url = articles_url.format(id,api_key)
    
    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response =  json.loads(get_articles_data)

        articles_results = None

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_articles(articles_results_list)

    return articles_results


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
        id = news_item.get('id')
        name = news_item.get('name')
        description = news_item.get('description')
        category = news_item.get('category')
        language = news_item.get('language')
        country = news_item.get('country')
        url = news_item.get('url')

        if description:
            news_object = News(id,name,description,category,language,country,url)
            news_sources.append(news_object)

    return news_sources

def process_articles(articles_list):
    '''
    '''
    articles_results = []
    for article in articles_list:
        id = article.get('id')
        author = article.get('author')
        title = article.get('title')
        description = article.get('description')
        url = article.get('url')
        image = article.get('urlToImage')
        
        
        if image:
            articles_object = Articles(id,author,title,description,url,image)
            articles_results.append(articles_object)
    
    return articles_results

# def search_news(wanted_news):
#     search_news_url = 'https://newsapi.org/v2/everything?apiKey={}&q={}'.format(api_key,wanted_news)

#     with urllib.request.urlopen(search_news_url) as url:
#         search_news_data = url.read()
#         search_news_response = json.loads(search_news_data)

#         search_news_results = None

#         if search_news_response['articles']:
#             search_news_list = search_news_response['articles']
#             search_news_results = process_sources(search_news_list)

#     return search_news_results