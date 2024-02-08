from bs4 import BeautifulSoup
import requests
import re

def scrape(target_url):
    data={}
    
    HEADERS={
            "accept-language": "en-US,en;q=0.9",
            "accept-encoding": "gzip, deflate, br",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
            }

    resp = requests.get(url=target_url, headers=HEADERS)
    soup = BeautifulSoup(resp.text, 'html.parser')

    try:
        data["title"]=soup.find('h1',{'id':'title'}).text.lstrip().rstrip()
    except:
        data["title"]=None

    images = re.findall('"hiRes":"(.+?)"', resp.text)
    data["image"]=""

    try:
        data["price"]=soup.find("span",{"class":"a-price"}).find("span").text
    except:
        data["price"]=None

    try:
        data["rating"]=soup.find("i",{"class":"a-icon-star"}).text
    except:
        data["rating"]=None

    return data