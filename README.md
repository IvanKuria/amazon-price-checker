
# Amazon Price Tracker

This Python script allows you to track the price of an item on Amazon and sends an email alert when the price drops below a specified threshold. The script uses BeautifulSoup for web scraping, requests to fetch the webpage, and smtplib for sending email notifications.

## Features
- Scrapes an Amazon product page for the current price.
- Compares the current price with your desired price.
- Sends an email alert when the price drops below a specified value.
- Simple and customizable.

## Requirements

- Python 3.x
- An Amazon product URL
- An SMTP email server (e.g., Gmail) for sending price alerts
- Environment variables for email credentials (recommended: `.env` file)

## Installation

1. **Clone this repository**:
   ```bash
   git clone https://github.com/yourusername/amazon-price-tracker.git
   ```

2. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the root of your project:
   ```
   EMAIL=your-email@gmail.com
   PASSWORD=your-email-password
   ```

4. **Modify the URL in the code**:
   Update the Amazon product URL in the script to the one you want to track.

## Usage

1. Run the script to check the price of the specified item:
   ```bash
   python price_tracker.py
   ```

2. If the price is below your target price (e.g., $110), an email notification will be sent to your inbox.

## Customization

- **Product URL**: Replace the URL variable with the Amazon product page of your choice.
- **Target Price**: Adjust the price threshold (default: $110) in the code as per your preference.
- **Recipient Email**: Set the recipient email address to where you want to receive the alerts.

## Example Code

Here is the basic logic for the price tracking:

```python
from bs4 import BeautifulSoup
import requests
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

# Replace with your product's Amazon URL
URL = "https://www.amazon.com/your-product-url"

# Request and scrape the product page
response = requests.get(URL, headers={{
    "User-Agent": "Mozilla/5.0",
    "Accept-Language": "en-US,en;q=0.9"
})

soup = BeautifulSoup(response.text, "html.parser")

# Extract price and product details
price_whole = soup.find(name="span", class_="a-price-whole").getText()
price_fraction = soup.find(name="span", class_="a-price-fraction").getText()
full_price = float(f"{price_whole}{price_fraction}")
product_title = soup.find(id="productTitle").getText().strip()

# Check if the price is below the threshold
if full_price < 110:
    message = f"{product_title} is now $110! Buy it here: {URL}"
else:
    message = "No price change."

# Send an email if price drops
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(EMAIL, PASSWORD)
    connection.sendmail(
        from_addr=EMAIL,
        to_addrs="recipient@example.com",
        msg=message
    )
```
