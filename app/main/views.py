from flask import render_template
from app import app

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
     # Getting bussiness news
    business_news = get_news('business')
    print(business_news)
    title = 'Home - Welcome to The News Review Website Online'
    return render_template('index.html', title = title, business = business_news)

    

