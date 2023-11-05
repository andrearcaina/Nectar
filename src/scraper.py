from src.scrapey import scrape
from src.scrapey_multi import get_data_info

def scraper(url):
    data = scrape(url)
    print(data)
    num = 2

    title = data['title']
    price = data['price']
    rating = data['rating']
    image = data['image']

    splitter = title.split(' ')
    links = []
    total_links = 0
    total_loops = 0
    while len(splitter) >= 1 or total_loops < 6:
        print(splitter)
        s = get_data_info(splitter, num)
        for i in s:
            if i[0] <= float(price[1:].replace(',', '')):
                links.append(i)
                total_links += 1
        if len(splitter) >= 1:
            splitter.pop(-1)
        if len(splitter) >= 1:
            splitter.pop(-1)
        total_loops += 1
    
    if total_links < num:
        rating = "high"
    elif total_links < num*3:
        rating = 'medium'
    else: 
        rating = 'low'
    

    # instead of return call get_data from scrapey_multi
    return (links, rating)

