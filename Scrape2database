import asyncio
from bs4 import BeautifulSoup
import requests
from prisma import Prisma

async def main():
    # Create an instance of the Prisma client
    db = Prisma()

    # Connect to the database
    await db.connect()

    # Fetch the HTML content from the website
    html_text = requests.get('https://www.groed.com/menu').text

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_text, 'lxml')

    # Find all the product div elements on the page
    products = soup.find_all('div', class_='FoodMenu_menuItem__E5KFQ')

    # Loop through each product
    for product in products:
        # Extract the product name
        product_name = product.find('h3', class_='FoodMenu_menuItemTitle__3cKia').text

        # Extract the product price
        product_price = product.find('div', class_='FoodMenu_menuItemPrice__caLBA').text.replace('.', '')

        # Add the product to the database
        await db.user.create(
            data={
                'name': product_name,
                'price': product_price
            }
        )

    # Print a message indicating that the data has been saved to the database
    print("Data saved to the database")

    # Disconnect from the database
    await db.disconnect()

# Run the main function asynchronously
if __name__ == '__main__':
    asyncio.run(main())
