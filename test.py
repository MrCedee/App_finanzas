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

with open("options.pkl", "rb") as op:
    options_data = pickle.load(op)
    
options_data["maxG"] = 20
print(options_data)

with open("options.pkl", "wb") as op:
    pickle.dump(options_data, op)