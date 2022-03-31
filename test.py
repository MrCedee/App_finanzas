from http.client import REQUESTED_RANGE_NOT_SATISFIABLE
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from tabulate import tabulate
import os
from bs4 import BeautifulSoup
import json
import requests
import time
import pickle

iri = "https://www.coingecko.com/es/monedas/tether/eur"
req = requests.get(iri)
sr = BeautifulSoup(req.content, "html.parser")

m = sr.find("span", class_="no-wrap").text
m = m[1:]
deur = float(m.replace(",", "."))

cuantities = [223.39, 0.003598, 336.66, 300, 111]
crypto = ["ada", "btc", "rose", "agix", "adax"]
urls = ["https://coinmarketcap.com/es/currencies/cardano/", "https://coinmarketcap.com/es/currencies/bitcoin/",
                "https://coinmarketcap.com/es/currencies/oasis-network/",
                "https://coinmarketcap.com/es/currencies/singularitynet/",
                "https://coinmarketcap.com/es/currencies/adax/"]
crypt_capital = []
prices = []
for cnt, ur in zip(cuantities, urls):
    c = requests.get(ur)
    soup = BeautifulSoup(c.content, "html.parser")
    b = soup.find(class_="priceValue").text.strip()
    b = b[1:]
    price = float(b.replace(",", ""))
    prices.append(price)
    crypt_capital.append(price * cnt * deur)
#prices = pd.Series(prices, name="Precio")
#crypt_capital = pd.Series(crypt_capital, name="Capital Crypto")
"""investment_data = pd.concat((cuantities, prices, crypt_capital), axis=1)
investment_data.index = crypto"""
investment_data = pd.DataFrame(columns=crypto, index=["Cantidad", "Euros", "Dólares"])
asa = [1,2,3,4,5]
investment_data.loc["Cantidad"] = cuantities
investment_data.loc["Euros"] = crypt_capital
investment_data.loc["Dólares"] = np.array(crypt_capital)/deur

print(investment_data)
