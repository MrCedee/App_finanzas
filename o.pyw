import pandas as pd
import numpy as np
record = pd.read_pickle("record.pkl")
d = pd.DataFrame(columns=["Gastos", "Ingresos"], index=["Total", "Media", "Desviación Típica"])
print(d)