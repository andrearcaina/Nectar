from src.scrapey import scrape
from src.scrapey_multi import get_data_info

def scraper(url):
    data = scrape(url)
    print(data)
    num = 1 

    title = data['title']
    price = data['price']
    rating = data['rating']
    #image = data['image']

    splitter = title.split(' ')
    links = []
    total_links = 0
    if len(splitter) > 1: #reduce specifiy
            splitter.pop(-1)
    if len(splitter) > 1: #reduce specifiy
            splitter.pop(-1)
    s = get_data_info(splitter, 5)
    
    if total_links < num*3:
        rating = "high"
    elif total_links < num*7:
        rating = 'medium'
    else: 
        rating = 'low'
    
    return (s, rating)

