from bs4 import BeautifulSoup
import requests
import smtplib
import os
from dotenv import load_dotenv


load_dotenv()
EMAIL = os.getenv("EMAIl")
PASSWORD =os.getenv("PASSWORD")

URL = ("https://www.amazon.com/Sceptre-24-5-inch-DisplayPort-FreeSync-E255B-FWD240/dp/B0CN1RDB18/ref=sr_1_3?crid"
       "=OFK3AS2KEV9J&dib=eyJ2IjoiMSJ9.EVMAGsFgffSSVwRdKUQPcxQg8ybFb-Uwh-g1axV_BrA-b16w8mZ-BO"
       "-lM7yq9CKtVoLmQ7jD1iB_C3cnBunseM14nwpo4Sqa7IZwR3UtUkXz365xUgaPXd6e5c3r4VajmyXATCV56KnC13yx3TEyzK8Y1vheb"
       "-sO575DPLS_btzACPSeD8l1LxoUVLjX0--ajzHYj_Ue8EmLNNV1I3fi0BjnrCYeCXGgQ2SeR14ZLt4"
       ".dHp58OCfIEzrrE6nEc0XXGMCcaKxvSXjzyC5FqQ72MQ&dib_tag=se&keywords=240%2Bhz%2Bmonitor%2B1440p%2B24%2Binch&qid"
       "=1725779248&sprefix=240%2Bhz%2B%2Caps%2C132&sr=8-3&th=1")

'''
Price Information
'''
response = requests.get(url=URL,
                        headers={
                            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, "
                                          "like Gecko)"
                                          "Chrome/128.0.0.0 Safari/537.36",
                            "Accept-Language": "en-US,en;q=0.9"
                        }
                        )

amazonWebpage = response.text

sp = BeautifulSoup(amazonWebpage, features="html.parser")

amazonPriceWhole = sp.find(name="span", class_="a-price-whole").getText()  # gets the whole number portion of the price

amazonPriceFraction = sp.find(name="span", class_="a-price-fraction").getText()  # gets the fraction portion of the
# price

amazonFullPrice = float(f"{amazonPriceWhole}{amazonPriceFraction}")  # combines the whole and fraction portions
amazonItemTitle = sp.find(id="productTitle").getText()

# checks whether current price is below our desired price
if amazonFullPrice < 110:
    message = f"{amazonItemTitle} is now $110 💰! Buy here: {URL}"
else:
    message = "No change in price 😢"

'''
Email Information
'''
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=EMAIL, password=PASSWORD)
    connection.sendmail(
        from_addr=EMAIL,
        to_addrs="harpercolins@yahoo.com",
        msg=message
    )
