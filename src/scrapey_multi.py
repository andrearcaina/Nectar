from bs4 import BeautifulSoup
import requests
import random

tags = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/100.0",

"Mozilla/5.0 (Windows NT 11.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/101.0",

"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4999.99 Safari/537.36",

"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/100.0",

"Mozilla/5.0 (Windows NT 11.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Safari/15.0",

"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Edge/101.0"]

# Function to extract Product Title
def get_title(soup):
	try:
		title = soup.find("span", attrs={"id":'productTitle'}).string.strip()

	except AttributeError:
		title_string = ""	

	return title_string

# Function to extract Product Price
def get_price(soup):
	try:
		price=soup.find("span",{"class":"a-price"}).find("span").text
	except:
		price=" Price not available"
	return price[1:].replace(',', '')

# Function to extract Product Rating
def get_rating(soup):
	try:
		rating = soup.find("i", attrs={'class':'a-icon a-icon-star a-star-4-5'}).string.strip()
		
	except AttributeError:
		
		try:
			rating = soup.find("span", attrs={'class':'a-icon-alt'}).string.strip()
		except:
			rating = "Price not available"	

	return rating[1:]

# Function to extract Number of User Reviews
def get_review_count(soup):
	try:
		review_count = soup.find("span", attrs={'id':'acrCustomerReviewText'}).string.strip()
		
	except AttributeError:
		review_count = ""	

	return review_count

# Function to extract Availability Status
def get_availability(soup):
	try:
		available = soup.find("div", attrs={'id':'availability'})
		available = available.find("span").string.strip()

	except AttributeError:
		available = "Not Available"	

	return available	

def get_data(prompt):
	results = []
	agentTag = tags[random.randint(0, 5)]
	HEADERS = ({'User-Agent':
					agentTag,
					'Accept-Language': 'en-US'})
	arr = []

	while (len(results) < 2):
		
		search = "+".join(prompt)

		URL = "https://www.amazon.com/s?k="+search+"&ref=nb_sb_noss_2"
		# HTTP Request
		webpage = requests.get(URL, headers=HEADERS)
		print(webpage)
		if webpage.status_code == 503: 
			agentTag = tags[random.randint(0, 5)]
			break
		# Soup Object containing all data
		soup = BeautifulSoup(webpage.content, "lxml")

		# Fetch links as List of Tag Objects
		links = soup.find_all("a", attrs={'class':'a-link-normal s-no-outline'}, limit=50)

		# Store the links
		links_list = []

		# Loop for extracting links from Tag Objects
		for link in links:
			links_list.append(link.get('href'))

		# Loop for extracting product details from each link 
		for link in links_list:
			print(link)
			if len(results) == 10:
				break
			new_webpage = requests.get("https://www.amazon.com" + link, headers=HEADERS)
			print('hel')
			new_soup = BeautifulSoup(new_webpage.content, "lxml")
			print('hell')
			price = get_price(new_soup)
			print(price)
			if price == "Price not available" or price == "":
				print("")
			else:
				print(price)
				arr = [float(price)]
				results.append(arr)
				print(results)
		if prompt != []:
			prompt.pop(-1)

	# the average price -- change algo later
	print(results)
	total = 0
	for r in results:
		total += r[0]
	total = total/10

	return total