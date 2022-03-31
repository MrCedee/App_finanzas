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

cuant = np.array([223.39, 0.003598, 336.66, 300, 111])
cuantities1 = pd.DataFrame(cuant)

print(cuantities1)