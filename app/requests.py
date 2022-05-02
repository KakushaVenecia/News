import urllib.request, json
from .models import Articles, Sources


#getting api key
api_key = None
base_url = None
articles_url = None

base_url= 'https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'
articles_url ='https://newsapi.org/v2/everything?language=en&sources={}&apiKey={}'

def configure_request(app):
    global api_key, base_url, articles_url
    api_key = app.config['NEWS_API_KEY']

def get_sources(category):
  
    get_sources_url =base_url.format(category, api_key)


    with urllib.request.urlopen(get_sources_url) as url_data:
        get_news_data = url_data.read()
        get_news_response = json.loads(get_news_data)
        news_results = None

        if get_news_response['sources']:
            news_results_list = get_news_response['sources']
            news_results = process_new_results(news_results_list)


    return news_results

def process_new_results(news_list):
    news_results =[]
    for news_item in news_list:
        id=news_item.get('id')
        name=news_item.get('name')
        description=news_item.get('description')
        url=news_item.get('url')
        category=news_item.get('category')
        country = news_item.get('country')
        language =news_item.get('language')

        news_object = Sources(id, name, description, url, category, country, language) 
        news_results.append(news_object)
    return news_results


def get_articles(source):	

    get_articles = articles_url.format(source, api_key)
    print('url: ' ,get_articles)
    with urllib.request.urlopen(get_articles) as url:
        articles_results =json.loads(url.read())
        articles_object = None
                
    if articles_results['articles']:
        articles_object = process_articles(articles_results['articles'])

    return articles_object

def process_articles(articles_list):
            
        articles_object = []
        for article_item in articles_list:
            id = article_item.get('id')
            author = article_item.get('author')
            title = article_item.get('title')
            description = article_item.get('description')
            url = article_item.get('url')
            url_image = article_item.get('urlToImage')
            date = article_item.get('publishedAt')
                
            if url_image:
                articles_result = Articles(id,author,title,description,url,url_image,date)
                articles_object.append(articles_result)	
            
        return articles_object