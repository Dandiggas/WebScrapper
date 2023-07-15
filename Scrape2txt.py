# Import required libraries
from bs4 import BeautifulSoup
import requests

# Create empty lists to store product names and prices
product_name_ls = []
product_price_ls = []

# Send a GET request to the URL and retrieve the HTML content
html_text = requests.get('https://www.groed.com/menu').text

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(html_text, 'lxml')

# Find all div elements with the specified class that contain product information
products = soup.find_all('div', class_='FoodMenu_menuItem__E5KFQ')

# Iterate over each product
for product in products:
    # Find the product name within the h3 element and extract the text
    product_name = product.find('h3', class_='FoodMenu_menuItemTitle__3cKia').text
    
    # Find the product price within the div element, remove the dot separator in the price text
    product_price = product.find('div', class_='FoodMenu_menuItemPrice__caLBA').text.replace('.', '')

    # Add the product name to the product_name_ls list
    product_name_ls.append(product_name)
    
    # Add the product price to the product_price_ls list
    product_price_ls.append(product_price)

# Open the "store.txt" file in write mode ('w')
with open("store.txt", 'w') as file:
    # Iterate over the zipped lists of product names and prices
    for name, price in zip(product_name_ls, product_price_ls):
        # Write the product name and price to the file, with a newline character at the end
        file.write(f"{name}: {price}\n")

# Print a message indicating that the data has been saved to the file
print("Data saved to store.txt")
