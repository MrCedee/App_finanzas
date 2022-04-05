import matplotlib.gridspec as gridspec
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

record = pd.read_pickle("record.pkl")

c = pd.concat((record["Gastos1"], record["Gastos2"], record["Gastos3"]))
print(c)
plt.hist(c, c.shape[0], (c.min(), c.max()))
plt.show()