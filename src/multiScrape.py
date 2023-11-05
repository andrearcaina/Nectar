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
        # Try to find the price using the "id" attribute
		price = soup.find("span", attrs={'id':'priceblock_ourprice'}).get_text().strip()
	except AttributeError:
		try:
            # If there is some deal price
			price = soup.find("span", {"class": "a-price"}).get_text().strip()
		except:
			price = "Price not available"

	return price

# Function to extract Product Rating
def get_rating(soup):

	try:
		rating = soup.find("i", attrs={'class':'a-icon a-icon-star a-star-4-5'}).string.strip()
		
	except AttributeError:
		
		try:
			rating = soup.find("span", attrs={'class':'a-icon-alt'}).string.strip()
		except:
			rating = ""	

	return rating

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


if __name__ == '__main__':

	# Headers for request
	HEADERS = ({'User-Agent':
	            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
	            'Accept-Language': 'en-US'})

	# The webpage URL
	URL = "https://www.amazon.com/s?k=iphone&ref=nb_sb_noss_2"
	
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
		links_list.append(link.get('href'))
		


	# Loop for extracting product details from each link 
	for link in links_list:
		if links_list[10] == link:
			break
		new_webpage = requests.get("https://www.amazon.com" + link, headers=HEADERS)

		new_soup = BeautifulSoup(new_webpage.content, "lxml")
		
		# Function calls to display all necessary product information
		print("Product Title =", get_title(new_soup))
		print("Product Price =", get_price(new_soup))
		print("Product Rating =", get_rating(new_soup))
		print("Number of Product Reviews =", get_review_count(new_soup))
		print("Availability =", get_availability(new_soup))
		print()
		print()