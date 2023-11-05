from bs4 import BeautifulSoup
import requests
import re

data={}
specs_dict={}

# example URL (can be changed later)
target_url="https://www.amazon.com/Bounty-Quick-Size-Paper-Towels-Family/dp/B079VP6DH5/ref=sr_1_1_sspa?keywords=paper+towels&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1"

HEADERS={
        "accept-language": "en-US,en;q=0.9",
        "accept-encoding": "gzip, deflate, br",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
        }

resp = requests.get(url=target_url, headers=HEADERS)
soup = BeautifulSoup(resp.text,'lxml')

try:
    data["title"]=soup.find('h1',{'id':'title'}).text.lstrip().rstrip()
except:
    data["title"]=None

images = re.findall('"hiRes":"(.+?)"', resp.text)
data["image"]=images[0]

try:
    data["price"]=soup.find("span",{"class":"a-price"}).find("span").text
except:
    data["price"]=None

try:
    data["rating"]=soup.find("i",{"class":"a-icon-star"}).text
except:
    data["rating"]=None


specs = soup.find_all("tr",{"class":"a-spacing-small"})

for i in range(len(specs)):
    spanTags = specs[i].find_all("span")
    specs_dict[spanTags[0].text]=spanTags[1].text

data["specs"]=specs_dict

for k,v in data.items():
    print(k,"|",v)