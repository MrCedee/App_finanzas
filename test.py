import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from tabulate import tabulate
import os
from bs4 import BeautifulSoup
import json
import requests
import time

def init_crypto():

    cuantities = pd.Series([223.39, 0.003598, 336.66, 300, 111], name="Cantidades")
    crypto = ["ada", "btc", "rose", "adax", "agix"]
    urls = ["https://coinmarketcap.com/es/currencies/cardano/", "https://coinmarketcap.com/es/currencies/bitcoin/", "https://coinmarketcap.com/es/currencies/oasis-network/", "https://coinmarketcap.com/es/currencies/singularitynet/", "https://coinmarketcap.com/es/currencies/adax/"]
    crypt_capital = []
    prices = []
    for cnt, ur in zip(cuantities, urls):

        c = requests.get(ur)
        soup = BeautifulSoup(c.content, "html.parser")
        b = soup.find(class_ = "priceValue").text.strip()
        b = b[1:]
        price = float(b.replace(",", ""))
        prices.append(price)
        crypt_capital.append(price * cnt)
    prices = pd.Series(prices, name="Precio")
    crypt_capital = pd.Series(crypt_capital, name="Capital Crypto")
    data = pd.concat((cuantities, prices, crypt_capital), axis=1)
    data.index = crypto


init_crypto()