from bs4 import BeautifulSoup
import requests
import random
import statistics
import math
import re


tags = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4999.99 Safari/537.36",

"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/101.0",

"Mozilla/5.0 (Windows NT 11.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/102.0",

"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_16_0) AppleWebKit/537.36 (KHTML, like Gecko) Safari/15.0",

"Mozilla/5.0 (Linux; Android 11; SM-G975U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4999.99 Mobile Safari/537.36",

"Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1"]

# Function to extract Product Title
def get_title(soup):
	try:
		title_string = soup.find("span", attrs={"id":'productTitle'}).string.strip()

	except AttributeError:
		title_string = ""	

	return title_string

#Function to extract image
def get_image(soup):
	images = re.findall('"hiRes":"(.+?)"', soup.text)
	image = ""
	if images != []: image=images[0]
	return image

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
			rating = "Rating not available"	

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

def get_data(prompt, num: int):
	results = []
	agentTag = tags[random.randint(0, 5)]
	HEADERS = ({'User-Agent':
					agentTag,
					'Accept-Language': 'en-US'})
	arr = []

	while (len(results) <= num) and prompt != []:
		
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
			if not ('/sspa' in link.get('href')):
				links_list.append(link.get('href'))

		# Loop for extracting product details from each link 
		for link in links_list:
			print(link)
			if len(results) > num:
				break
			new_webpage = requests.get("https://www.amazon.com" + link, headers=HEADERS)
			print('hel')
			new_soup = BeautifulSoup(new_webpage.content, "lxml")
			print('hell')
			price = get_price(new_soup)
			# rating = get_rating(new_soup)
			# review = get_review_count(new_soup)
			# availability = get_availability(new_soup)
			# image = get_image(new_soup)
			print(price)
			if price == "Price not available" or price == "":
				print("")
			else:
				print(price)
				arr = [float(price)] #, rating, review, availability, image]
				results.append(arr)
				print(results)
		if prompt != []:
			prompt.pop(-1)

	# the average price -- change algo later
	print(results)
	results_pricing = []
	total = 0
	for r in results:
		results_pricing.append(r[0]) 
		total += r[0]

	sd = statistics.stdev(results_pricing)
	total = total/(num+1)
	
	return total

def get_data_info(prompt, num: int):
	results = []
	agentTag = tags[random.randint(0, 5)]
	HEADERS = ({'User-Agent':
					agentTag,
					'Accept-Language': 'en-US'})
	arr = []

	while (len(results) <= num) and prompt != []:
		
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
			if not ('/sspa' in link.get('href')):
				links_list.append(link.get('href'))

		# Loop for extracting product details from each link 
		for link in links_list:
			print(link)
			if len(results) > num:
				break
			new_webpage = requests.get("https://www.amazon.com" + link, headers=HEADERS)
			new_soup = BeautifulSoup(new_webpage.content, "lxml")
			price = get_price(new_soup)
			# rating = get_rating(new_soup)
			# review = get_review_count(new_soup)
			# availability = get_availability(new_soup)
			title = get_title(new_soup)
			image = get_image(new_soup)
			print(price)
			if price == "Price not available" or price == "":
				print("")
			else:
				arr = [float(price), title, image, "https://www.amazon.com" + link] #, rating, review, availability, image]
				results.append(arr)
				print(results)
		if prompt != []:
			prompt.pop(-1)
	
	return results