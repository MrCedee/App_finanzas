import numpy as np
import pandas as pd
import datetime as dt
pd.options.display.max_columns=20
pd.options.display.max_rows=100
day1=np.datetime64("2021-12-13",'D')
day2=np.datetime64("2022-02-28","D")
delta=np.timedelta64(1,'W')
days=pd.Series(np.arange(day1,day2,delta), name="Weeks")
concepto1=[""]*11
concepto2=[""]*11
concepto3=[""]*11
concepto1[0]="Regalos"
concepto2[0]="Comida"
concepto1[1]="Actividades"
concepto1[2]="Regalos"
concepto2[2]="Indefinido"
concepto1[3]="Comida"
concepto1[4]="Comida"
concepto2[4]="Tecnología"
concepto1[5]="Celebraciones"
concepto2[5]="Actividades"
concepto1[6]="Actividades"
concepto1[8]="Pareja"
concepto2[8]="Comida"
concepto1[9]="Comida"
concepto3[5]="Pareja"

gastos1=[100,47.86,17.81,16.48,12.69,10,21.74,0,25,27.45,0]

gastos2=[25,0,16.18,0,30,63.98,0,0,8.3,0,0]

gastos3=[0]*11
gastos3[5]=30

ingresos1=[50]*11
concepto_1=["Paga"]*11
ingresos2=[0]*11
concepto_2=[""]*11
concepto_2[5]="Regalo"
ingresos2[5]=150


traspasos=[10,25,18.82,8.52,12.31,25,25,25,0,19.96,5]
descripcion_t=["g a b"]*11
descripcion_t[0]="b a g"
descripcion_t[8]=""
ahorro=[0]*11
ahorro[2]=20
ahorro[8]=100
ahorro[10]=62.09

capitalb=[0]*11
capitalg=[0]*11
capitala=[517.91]*11
capitalb[0]=5
capitalg[0]=10

capitalb=[5,7.14,13.15,46.67,83.98,150,178.26,228.26,144.96,150,117.91]
capitalg=[10,10,0,0,0,0,0,0,0,17.51,37.51]
for i in range(1,11):
    capitala[i]=capitala[i-1]+ahorro[i]

record=pd.DataFrame(index=days)
record["Concepto1"]=concepto1
record["Gastos1"]=gastos1
record["Concepto2"]=concepto2
record["Gastos2"]=gastos2
record["Concepto3"]=concepto3
record["Gastos3"]=gastos3
record["Concepto_1"]=concepto_1
record["Ingresos1"]=ingresos1
record["Concepto_2"]=concepto_2
record["Ingresos2"]=ingresos2
record["Descripción"]=descripcion_t
record["Traspasos"]=traspasos
record["Ahorro"]=ahorro
record["Capital bancario"]=capitalb
record["Capital gasto"]=capitalg
record["Capital ahorrado"]=capitala
record=record.convert_dtypes()
record.to_pickle("record_p.pkl")
