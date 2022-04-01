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

options = {"Crypto": True, "Axis": 3}

with open("options.pkl", "wb") as op:
    pickle.dump(options, op)

with open("options.pkl", "rb") as op:
    options_data = pickle.load(op)
if options_data["Crypto"]:
    print(options_data)