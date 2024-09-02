import requests
from bs4 import BeautifulSoup
import pandas as pd

# Function to scrape product information
def scrape_products(url):
    # Send a GET request to the webpage
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Lists to store product data
    product_names = []
    product_prices = []
    product_ratings = []

    # Find all product containers (this will depend on the website's HTML structure)
    products = soup.find_all('div', class_='product')  # Adjust the class name as necessary

    for product in products:
        # Extract product name
        name = product.find('h2', class_='product-name').text.strip()  # Adjust the tag/class name
        product_names.append(name)

        # Extract product price
        price = product.find('span', class_='product-price').text.strip()  # Adjust the tag/class name
        product_prices.append(price)

        # Extract product rating
        rating = product.find('span', class_='product-rating').text.strip()  # Adjust the tag/class name
        product_ratings.append(rating)

    # Create a DataFrame and save to CSV
    df = pd.DataFrame({
        'Name': product_names,
        'Price': product_prices,
        'Rating': product_ratings
    })

    df.to_csv('products.csv', index=False)
    print("Data saved to products.csv")

# URL of the e-commerce website's product listing page
url = 'https://example.com/products'  # Replace with the actual URL
scrape_products(url)