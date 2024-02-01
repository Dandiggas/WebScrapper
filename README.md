# WebScrapper for Porridge Shop in Denmark

## Overview
This WebScrapper is a Flask-based application designed to scrape product names and prices from a specific porridge shop's website in Denmark. It utilizes Beautiful Soup for scraping the website, saves the data in a PostgreSQL database, and exposes the data through a Flask API.

## Features
- **Data Scraping**: Extracts product names and prices from the website.
- **Data Storage**: Stores the scraped data in a PostgreSQL database.
- **API Endpoint**: Provides an API endpoint to access the product information.

## Prerequisites
- Docker
- Git

## Installation

1. **Clone the Repository**
    ```bash
    git clone https://github.com/Dandiggas/WebScrapper
    ```

2. **Navigate to the Project Directory**
    ```bash
    cd /Webscrapper
    ```

3. **Docker Compose**
    ```bash
    docker compose up -d
    ```

## Usage

The application provides two main endpoints:

- **Get All Products**: Retrieves all products from the database.
    ```
    GET /getproducts
    ```
    Response: 
    ```json
    { "users": [{...}, {...}] }
    ```

- **Get Single Product**: Retrieves details of a single product by ID.
    ```
    GET /getproduct
    ```
    Response:
    ```json
    { "product_detail": {...} }
    ```

## API Reference

The API is built using Flask and offers the following endpoints:

- `/getproducts`: Method `GET`. Returns a list of all products.
- `/getproduct`: Method `GET`. Returns a single product detail.

## Development

To run the application in development mode:

```bash
flask run --debug
```

## Contributing
Contributions to this project are welcome. Please follow the standard fork, branch, and pull request workflow.
