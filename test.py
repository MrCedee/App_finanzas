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

r = {"Indices": 1, "Cryptos": 0}
with open("options.pkl", "wb") as op:
    pickle.dump(r, op, pickle.HIGHEST_PROTOCOL)

with open("options.pkl", "rb") as op1:
    m = pickle.load(op1)

print(m)
