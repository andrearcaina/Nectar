from bs4 import BeautifulSoup
import requests

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
	HEADERS = ({'User-Agent':
					'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Safari/14.1.2',
					'Accept-Language': 'en-US'})
	arr = []

	while (len(results) < 10):
		
		search = "+".join(prompt)

		URL = "https://www.amazon.com/s?k="+search+"&ref=nb_sb_noss_2"
		# HTTP Request
		webpage = requests.get(URL, headers=HEADERS)
		print(webpage)
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
				exit
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
	total = sum(results[0])/10

	return total