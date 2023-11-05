from src.scrapey import scrape
from src.scrapey_multi import get_data

def scraper(url):
    data = scrape(url)
    print(data)

    title = data['title']
    price = data['price']
    rating = data['rating']
    image = data['image']

    # instead of return call get_data from scrapey_multi
    return [title, price, rating, image]

