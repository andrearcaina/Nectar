from src.scrapey import scrape
from src.scrapey_multi import get_data_info

def scraper(url):
    data = scrape(url)
    print(data)
    num = 1 #get info param

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
    # for i in range(0, 5):
    #     print(splitter)
    #     s = get_data_info(splitter, num) # list of info of scraped objects
    #     for n in s: # the specifci scarped obj
    #         if n[0] <= float(price[1:].replace(',', '')): #0 is price
    #             links.append(n)
    #             total_links += 1
    #     if len(splitter) > 1: #reduce specifiy
    #         splitter.pop(-1)
    #        # splitter.pop(0) #optional
       
    
    if total_links < num*3:
        rating = "high"
    elif total_links < num*7:
        rating = 'medium'
    else: 
        rating = 'low'
    

    # instead of return call get_data from scrapey_multi
    return (s, rating)

