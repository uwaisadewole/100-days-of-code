from bs4 import BeautifulSoup
import requests
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os

load_dotenv()

HOST = os.getenv("SMTP_SERVER")
PORT = os.getenv("SMTP_PORT")
SENDER = os.getenv("ADMIN_MAIL")
PASS = os.getenv("EMAIL_PASS")
LINK = "https://www.amazon.com/dp/B075CYMYK6?lv=shuf&channelId=751&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&plpRedirect=mhFallback&th=1"



target_price = 150000

headers = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:159.0) Gecko/20100101 Firefox/159.0",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Te":	"trailers",
    "Upgrade-Insecure-Requests": "1",
}

response = requests.get(url=LINK, headers=headers)
html = response.text



soup = BeautifulSoup(html, "html.parser")
price_o = soup.find("span", class_="a-offscreen")
price = price_o.getText().replace("NGN", "")
price = round(float(price.replace(",", "")))


if price < target_price:
    smtp_host = HOST
    smtp_port = PORT
    sender_mail = SENDER
    password = PASS

    with smtplib.SMTP(smtp_host, smtp_port) as connection:
        connection.starttls()
        connection.login(user=sender_mail, password=password)
        msg = EmailMessage()
        msg["Subject"] = "There is a reduction in price for this product"
        msg["From"] = sender_mail
        msg["To"] = "uakmail1307@gmail.com"
        msg.set_content(f"Instant Pot Duo Plus 9-in-1 Electric Pressure Cooker, Slow Cooker, Rice Cooker, Steamer, Sauté, Yogurt Maker, Warmer & Sterilizer, Includes App With Over 800 Recipes, Stainless Steel, 3 Quart is now {price_o.getText()}")
        connection.send_message(msg)
        print("Success: Email sent!")
