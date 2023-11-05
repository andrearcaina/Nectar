from bs4 import BeautifulSoup
import requests

# Function to extract Product Title
def get_title(soup):
	
	try:
		# Outer Tag Object
		title = soup.find("span", attrs={"id":'productTitle'})

		# Inner NavigatableString Object
		title_value = title.string

		# Title as a string value
		title_string = title_value.strip()

		# # Printing types of values for efficient understanding
		# print(type(title))
		# print(type(title_value))
		# print(type(title_string))
		# print()

	except AttributeError:
		title_string = ""	

	return title_string

# Function to extract Product Price
def get_price(soup):

	try:
		price=soup.find("span",{"class":"a-price"}).find("span").text
	except: 
		price=" Price not available"

	return price[1:].replace(',','')

# Function to extract Product Rating
def get_rating(soup):

	try:
		rating = soup.find("i", attrs={'class':'a-icon a-icon-star a-star-4-5'}).string.strip()
		
	except AttributeError:
		
		try:
			rating = soup.find("span", attrs={'class':'a-icon-alt'}).string.strip()
		except:
			rating = ""	

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
					'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.9999.99 Safari/537.36',
					'Accept-Language': 'en-US'})

	while (len(results) < 10):
		
		search = "+".join(prompt)

		URL = "https://www.amazon.com/s?k="+search+"&ref=nb_sb_noss_2"

		# HTTP Request
		webpage = requests.get(URL, headers=HEADERS)

		# Soup Object containing all data
		soup = BeautifulSoup(webpage.content, "lxml")

		# Fetch links as List of Tag Objects
		links = soup.find_all("a", attrs={'class':'a-link-normal s-no-outline'})

		# Store the links
		links_list = []

		# Loop for extracting links from Tag Objects
		for link in links:
			if link == links[10]:
				break
			links_list.append(link.get('href'))

		# Loop for extracting product details from each link 
		for link in links_list:
			print(link)
			if len(results) == 10:
				break
			new_webpage = requests.get("https://www.amazon.com" + link, headers=HEADERS)
			new_soup = BeautifulSoup(new_webpage.content, "lxml")
			price = get_price(new_soup)
			print(price)
			if price == "Price not available" or price == "":
				print("")
			else:
				arr = [float(price)]
				results.append(arr)
		if prompt != []:
			prompt.pop(-1)

	# the average price -- change algo later
	print(sum(arr))
	total = sum(arr)/10

	return total