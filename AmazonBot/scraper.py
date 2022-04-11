import requests
from telegram.ext import *
from bs4 import BeautifulSoup
import time

# URL = 'https://www.amazon.it/ZOTAC-GAMING-GeForce-3070-Twin/dp/B08LBVNKT1/ref=sr_1_5?__mk_it_IT=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=3070&qid=1620997513&sr=8-5'

headers = {"User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}


def check_price(URL):
    page = requests.get(URL, headers = headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id = "productTitle").get_text()

    if(soup.find(id = "priceblock_ourprice")):
        price = soup.find(id = "priceblock_ourprice").get_text()
        converted_price = float(price[0:5])

        if(converted_price < 3.000):
            send_telegramMessage(URL, title, price)
    else:
        print("")
        

def send_telegramMessage(URL, title, price):
    updater = Updater(keys.APYKey, use_context = True)
    update.message.reply_text("il prezzo di " + title.strip() + " e` " + price.strip())