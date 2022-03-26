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
concepto1[8]="Natalia"
concepto2[8]="Comida"
concepto1[9]="Comida"
concepto3[5]="Natalia"

gastos1=[10,47.86,17.81,16.48,12.69,10,21.74,0,25,27.45,0]

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
record.to_pickle("record.pkl")


import numpy as np
import pandas as pd
import os
from tabulate import tabulate
import warnings
warnings.filterwarnings("ignore")
def inicio():
    global p, p2, o, k
    while k!=0:
        for i in p:
            print(i.center(width))
        for i in p2:
            print(i.center(width))
        k = input(o.rjust(round(width / 2) + 5, " "))
        os.system("cls")
        if k=="A" or k=="a":
            a()
        elif k=="B" or k=="b":
            b()
        elif k=="C" or k=="c":
            c()
        else: k=0
def a():
    global g, e,record, o, width,m7,m8,k
    while k!=0 and k!=1:
        print(g.center(width, "-"))
        print(g.center(width, "-"))
        print(e)
        print(tabulate(record, headers='keys', tablefmt='pretty'))
        print(e)
        print(g.center(width, "-"))
        print(g.center(width, "-"))
        print(e)
        print(e)
        print(e)
        print("B - Volver Al Inicio".center(width))
        print("=   ====== == ======".center(width))
        print(m7.center(width))
        print(m8.center(width))
        print(e)
        print(e)
        k = input(o.rjust(round(width / 2) + 5, " "))
        os.system("cls")
        if k=="b" or k=="B":
            k=1
        else: k=0
def b():
    global record,e,m7,m8,width,o,k
    while k!=0 and k!=1:
        a1="A - Nueva Semana"
        a2="=   ===== ======"
        a3="B - Semana Anterior"
        a4="=   ====== ========"
        p1=[e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,a1,a2,e,a3,a4,e,"C - Volver Al Inicio","=   ====== == ======",e,m7,m8,e,e,e]
        for i in p1:
            print(i.center(width))
        k = input(o.rjust(round(width / 2) + 5, " "))
        os.system("cls")
        if k=="A" or k=="a":
            delta = np.timedelta64(1, 'W')
            day = np.datetime64(record.index[-1], "D") + delta
            capitalb=record["Capital bancario"].iloc[-1]
            capitalg=record["Capital gasto"].iloc[-1]
            capitala=record["Capital ahorrado"].iloc[-1]
            for i in range(15):
                print(e)
            c=[]
            for i in range(len(record.columns)):
                if i!=0:
                    if c[i-1]=="":
                        c.append(0)
                        continue
                j=record.columns[i]
                v=input(j.rjust(round(width / 2) + 5, " ")+": ")
                if record[j].dtype=="string":
                    c.append(v)
                else:
                    if v=="": v=0
                    if float(v)!= float(0):
                        if i<11:
                            if i<6:
                                pr="b o g: "
                                v1 = input(pr.rjust(round(width / 2) + 5, " "))
                                if v1=="b" or v1== "B":
                                    capitalb-=float(v)
                                if v1=="g" or v1== "G":
                                    capitalg-=float(v)
                            else:
                                pr="banco: "
                                v1 = float(input(pr.rjust(round(width / 2) + 5, " ")))
                                capitalb+=v1
                                pr = "gasto: "
                                v1 = float(input(pr.rjust(round(width / 2) + 5, " ")))
                                capitalg += v1
                        if i==11:
                            if c[i-1]=="b a g":
                                capitalb-=float(v)
                                capitalg+=float(v)
                            elif c[i-1]=="g a b":
                                capitalg-=float(v)
                                capitalb+=float(v)


                    c.append(float(v))
                if j=="Ahorro":
                    pr = "banco: "
                    capitalb-=float(v)
                    capitala+=float(v)
                    break
            c.append(capitalb)
            c.append(capitalg)
            c.append(capitala)
            record.loc[day]=c
            os.system("cls")
        elif k=="B" or k=="b":
            print(g.center(width, "-"))
            print(g.center(width, "-"))
            print(e)
            print(tabulate(record, headers='keys', tablefmt='pretty'))
            print(e)
            print(g.center(width, "-"))
            print(g.center(width, "-"))
            print(e)
            print(e)
            print(e)
            j="Escriba la fecha de los datos a modificar siguiedo el formato YYYY-MM-DD"
            v = input(j.rjust(round(width / 2) + 5, " ") + ": ")
            if v in record.index:
                part=record.loc[v]
                print(e)
                print(e)
                j="Modificar (g)astos, (i)ngresos, (t)raspaso o (a)horro"
                v1=input(j.rjust(round(width / 2) + 5, " ") + ": ")
                if v1=="g" or v1=="G":
                    print(e)
                    j = "Inserte cantidad de gasto1, si no inserta nada se mantendra la actual"
                    v2 = input(j.rjust(round(width / 2) + 5, " ") + ": ")
                    if v2!="":
                        print(e)
                        j = "Concepto"
                        v3 = input(j.rjust(round(width / 2) + 5, " ") + ": ")
                        part["Concepto1"]=v3
                        part["Gastos1"]=float(v2)
                    print(e)
                    j = "Inserte cantidad de gasto2, si no inserta nada se mantendra la actual"
                    v2 = input(j.rjust(round(width / 2) + 5, " ") + ": ")
                    if v2!="":
                        print(e)
                        j = "Concepto"
                        v3 = input(j.rjust(round(width / 2) + 5, " ") + ": ")
                        part["Concepto2"]=v3
                        part["Gastos2"]=float(v2)
                    print(e)
                    j = "Inserte cantidad de gasto3, si no inserta nada se mantendra la actual"
                    v2 = input(j.rjust(round(width / 2) + 5, " ") + ": ")
                    if v2!="":
                        print(e)
                        j = "Concepto"
                        v3 = input(j.rjust(round(width / 2) + 5, " ") + ": ")
                        part["Concepto3"]=v3
                        part["Gastos3"]=float(v2)
                elif v1=="i" or v1=="I":
                    print(e)
                    j = "Inserte cantidad de Ingreso1, si no inserta nada se mantendra la actual"
                    v2 = input(j.rjust(round(width / 2) + 5, " ") + ": ")
                    if v2 != "":
                        print(e)
                        j = "Concepto"
                        v3 = input(j.rjust(round(width / 2) + 5, " ") + ": ")
                        part["Concepto_1"] = v3
                        part["Ingresos1"] = float(v2)
                    print(e)
                    j = "Inserte cantidad de Ingreso2, si no inserta nada se mantendra la actual"
                    v2 = input(j.rjust(round(width / 2) + 5, " ") + ": ")
                    if v2 != "":
                        print(e)
                        j = "Concepto"
                        v3 = input(j.rjust(round(width / 2) + 5, " ") + ": ")
                        part["Concepto_2"] = v3
                        part["Ingresos2"] = float(v2)
                elif v1=="t" or v1=="T":
                    print(e)
                    j = "Inserte la descripción"
                    v2 = input(j.rjust(round(width / 2) + 5, " ") + ": ")
                    if v2=="b a g" or v2=="g a b":
                        part["Descripción"]=v2
                        print(e)
                        j = "Inserte la cantidad"
                        v3 = input(j.rjust(round(width / 2) + 5, " ") + ": ")
                        part["Traspasos"]=float(v2)
                        if v2 == "b a g":
                            part["Capital bancario"]-=float(v3)
                            part["Capital gasto"]+=float(v3)
                        else:
                            part["Capital bancario"]+=float(v3)
                            part["Capital gasto"]-=float(v3)
                elif v1=="a" or v1=="A":
                    print(e)
                    j = "Inserte la cantidad"
                    v2 = input(j.rjust(round(width / 2) + 5, " ") + ": ")
                    part["Ahorro"] = float(v2)
                    part["Capital bancario"]-=float(v2)
                    part["Capital ahorrado"]+=float(v2)

                partition=record.loc[v:]

                dcb=part["Capital bancario"]-record["Capital bancario"].loc[v]
                dcg=part["Capital gasto"]-record["Capital gasto"].loc[v]
                dca=part["Capital ahorrado"]-record["Capital ahorrado"].loc[v]
                partition["Capital bancario"]+=dcb
                partition["Capital gasto"]+=dcg
                partition["Capital ahorrado"]+=dca
                partition.loc[v]=part
                record.loc[v:] = partition
        elif k=="C" or k=="c":
            k=1
        else: k=0

os.system("color 0a")
os.system("cls")
pd.options.display.max_columns=20
pd.options.display.max_rows=100
pd.options.display.width = 1000
width=os.get_terminal_size()
width=width[0]
record=pd.read_pickle("record.pkl")
e=""
g="---------------------------------------------------------------------------------------------------------------------------------------------------------------------"
l1="####### ### ###  ##  ####### ###  ##   ###### ###  ####### ###        ######   #####  ###  ### ###  ## #########     ##### ###  ###   ##### ######### ####### ##   ##"
l2="##      ### #### ##  ##   ## #### ##  ###     ###  ##   ## ###       ###      ##   ## ###  ### #### ##    ###       ###    ###  ###  ###       ###    ##      ### ###"
l3="####### ### #######  ####### #######  ###     ###  ####### ###       ###      ##   ## ###  ### #######    ###       ###    ########  ###       ###    ####### #######"
l4="##      ### ### ###  ##   ## ### ###  ###     ###  ##   ## ###       ###      ##   ## ###  ### ### ###    ###       ###      ###     ###       ###    ###     ## # ##"
l5="##      ### ###  ##  ##   ## ###  ##   ###### ###  ##   ## #######    ######   #####    ####   ###  ##    ###    #####       ###  #####        ###    ####### ##   ##"
p=[g,g,e,l1,l2,l3,l4,l5,e,g,g]
o = "Option: "

m1="A - Ver Estado"
m2="=   === ======"
m3="B - Agregar Datos"
m4="=   ======= ====="
m5="C - Obtener Métricas"
m6="=   ======= ========"
m7="Other - Salir"
m8="=====   ====="

p2=[e,e,e,m1,m2,e,m3,m4,e,m5,m6,e,m7,m8,e,e,e]
k=1
inicio()
