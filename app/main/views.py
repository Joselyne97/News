from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_newss,get_articles
# from .forms import ReviewForm
# from ..models import Review
from ..models import News

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
     # Getting bussiness news
    business_news = get_newss('business')
    technology_news = get_newss('technology')
    sports_news = get_newss('sports')
    general_news = get_newss('general')
    entertainment_news = get_newss('entertainment')
    health_news = get_newss('health')
    science_news = get_newss('science')

    title = 'Home - Welcome to The News Review Website Online'
    # search_news = requests.args.get('news_query')
    # if search_news:
    #     return redirect(url_for('main.search',wanted_news = search_news))
    # else:
    return render_template('index.html', title = title, business_news = business_news, technology_news = technology_news,sports_news = sports_news, general_news = general_news, entertainment_news = entertainment_news, health_news = health_news, science_news = science_news)

@main.route('/articles/<id>')
def articles(id):
   '''
   view articles page
   '''
  
   articles = get_articles(id)
  
   title = 'Home - Welcome to The News Review Website Online those are articles'
   return render_template('articles.html',title= title,articles = articles)

