from bs4 import BeautifulSoup
import requests
import re

def scrape(target_url):
    data = {}
    
    HEADERS = {
        "accept-language": "en-US,en;q=0.9",
        "accept-encoding": "gzip, deflate, br",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
    }

    try:
        resp = requests.get(url=target_url, headers=HEADERS)
        resp.raise_for_status()  # Raise HTTPError for non-2xx status codes

        soup = BeautifulSoup(resp.text, 'html.parser')

        # Extract title
        title_tag = soup.find('h1', {'id': 'title'})
        data["title"] = title_tag.text.strip() if title_tag else None

        # Extract images
        images = re.findall('"hiRes":"(.+?)"', resp.text)
        data["images"] = images if images else None

        # Extract price
        price_tag = soup.find("span", {"class": "a-price"})
        data["price"] = price_tag.find("span").text.strip() if price_tag else None

        # Extract rating
        rating_tag = soup.find("i", {"class": "a-icon-star"})
        data["rating"] = rating_tag.text.strip() if rating_tag else None

    except requests.RequestException as e:
        print(f"Error fetching URL: {e}")
        data = None

    return data
