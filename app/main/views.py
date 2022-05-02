from operator import index
from flask import render_template,request,url_for
from . import main
from ..requests import get_sources, get_articles
from ..models import Sources


"""
https://newsapi.org/v2/everything?q=bitcoin&apiKey={}

https://newsapi.org/v2/sources?language=en&category={}&apiKey={}%27
"""

@main.route('//')
def index():
	
    general_info= get_sources('general')
    technology= get_sources('technology')
    sports = get_sources('sports')
    entertainment= get_sources('entertainment')
    return render_template('index.html',general_info = general_info, technology= technology, sports = sports, entertainment =entertainment )


@main.route('/sources/<id>')
def articles(id):
	'''
	view articles page
	'''
	articles = get_articles(id)
	title = f'NH | {id}'

	return render_template('articles.html',title= title,articles = articles)
