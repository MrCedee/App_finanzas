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

i=np.arange(1,10,1)
j = np.arange(1,20,0.5)
plt.subplot(2,2,(1,2))
plt.plot(i,i)

plt.subplot(2,2,(3,4))
plt.plot(j,j)

plt.show()