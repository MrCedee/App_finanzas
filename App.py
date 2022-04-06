import numpy as np
import pandas as pd
import os
from tabulate import tabulate
import warnings
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import keyboard
import requests
from bs4 import BeautifulSoup
import pickle 
import time


class App:
    def __init__(self):
        keyboard.press("f11")
        os.system("color 0e")
        os.system("cls")
        pd.options.display.max_columns = 20
        pd.options.display.max_rows = 100
        pd.options.display.width = 1000
        pd.set_option("display.precision", 2)
        self.width = os.get_terminal_size()
        self.width = self.width[0]
        self.record = pd.read_pickle("record.pkl")
        self.state = -1
        self.ask = 0
        self.o = "Option: "
        self.g = "-".center(self.width, "-")
        warnings.filterwarnings("ignore")
        self.oli = "Press any button to go back "
        self.e = ""
        self.patrimonio = 0
        self.options_data = 0
        self.deur = 0
        self.crypto = 0
        self.cuantities = 0
        self.cuantities = np.load("cuantities.npy")
        self.dolar_euro()
        self.options_init()
        
    def dolar_euro(self):
        iri = "https://www.coingecko.com/es/monedas/tether/eur"
        req = requests.get(iri)
        sr = BeautifulSoup(req.content, "html.parser")
        m = sr.find("span", class_="no-wrap").text
        m = m[1:]
        self.deur = float(m.replace(",", "."))
        
    def confirm(self):
        os.system("cls")
        for _ in range(50):
                print(self.e)
        w = "Exit?"
        print(w.center(self.width))
        print(self.e)
        w = "Y or N: "
        t = input(w.rjust(round(self.width / 2)))
        if t.lower() =="n":
            os.system("cls")
            return False
        else:
            return True    
    
    def options(self):
        os.system("cls")
        self.state = 2
        while self.state != 0 and self.state != 1:
            self.state = 2
            for i in range(5):
                print(self.e)
        
            self.opciones(["Mostrar Cryptos, Actual: " + str(self.options_data["Crypto"]), "Opciones de indices, Actual: " + str(self.options_data["Axis"]), "Objetivo Máximo de Gasto, Actual: " + str(self.options_data["maxG"])])
            self.ask = input(self.o.rjust(round(self.width / 2) + 5, " "))
            if self.ask.lower() == "a":
                self.options_data["Crypto"] = not self.options_data["Crypto"]
            elif self.ask.lower() == "b":
                t = ["Cantidad de indices en Gráficos reducida: 1", "Cantidad de indices media: 2", "Cantidad de indices total: 3"]
                for i in t:
                    print(i.center(self.width))
                ask1 = input(self.o.rjust(round(self.width / 2) + 5, " "))
                os.system("cls")
                if ask1 == "1" or ask1 == "2" or ask1 == "3":
                    self.options_data["Axis"] = int(ask1)
            elif self.ask.lower() == "c":
                iu = "Nueva cantidad: "
                self.ask1 = input(iu.rjust(round(self.width / 2) + 5, " "))
                try: 
                    self.options_data["maxG"] = float(self.ask1)
                except:
                    os.system("cls")
                    for i in range(15):
                        print(self.e)
                    print("Cannot convert to float".center(self.width))
                    time.sleep(5)
                    os.system("cls")
            elif self.ask.lower() == "d":
                self.state = 1
            else:
                self.state = 0
            
        with open("options.pkl", "wb") as op:
            pickle.dump(self.options_data, op)
        os.system("cls")

    def options_init(self):
        with open("options.pkl", "rb") as op:
            self.options_data = pickle.load(op)

    def rounddf(self):
        self.record["Capital bancario"] = self.record["Capital bancario"].astype("float").round(2)
        self.record["Capital gasto"] = self.record["Capital gasto"].astype("float").round(2)
        self.record["Capital ahorrado"] = self.record["Capital ahorrado"].astype("float").round(2)
        self.record["Gastos1"] = self.record["Gastos1"].astype("float").round(2)
        self.record["Gastos2"] = self.record["Gastos2"].astype("float").round(2)
        self.record["Gastos3"] = self.record["Gastos3"].astype("float").round(2)
        self.record["Ingresos1"] = self.record["Ingresos1"].astype("float").round(2)
        self.record["Ingresos2"] = self.record["Ingresos2"].astype("float").round(2)
        self.record["Ahorro"] = self.record["Ahorro"].astype("float").round(2)
        self.record["Traspasos"] = self.record["Traspasos"].astype("float").round(2)

    def opciones(self, lista: list, margen: int = 23, condicion: bool =True):
        aux = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
               'V', "W", "X", "Y", "Z"]
        for i in range(margen - len(lista)):
            print(" ")
        for i in range(len(lista)):
            l = []
            m = aux[i] + " " + "-" + " " + lista[i]
            _ = "=   "
            l.append(_)
            for j in lista[i].split():
                _ = ["="] * len(j)
                l.extend(_)
                l.append(" ")
            l.pop()
            print(m.center(self.width))
            print("".join(l).center(self.width))
            print(" ")
        if condicion:
            m = aux[i + 1] + " - Volver atrás"
            print(m.center(self.width))
            print("=   ====== =====".center(self.width))
            print(" ")
        print("Other - Salir".center(self.width))
        print("=====   =====".center(self.width))
        print(" ")
        print(" ")
        print(" ")

    def customize_cryptos(self):
        self.state = 3
        while self.state != 2 and self.state != 0:
            self.state = 3
            os.system("cls")
            self.opciones(["Elegir Crypto"])
            self.ask = input(self.o.rjust(round(self.width / 2) + 5, " "))
            if self.ask.lower() == "a":
                aux = pd.DataFrame(self.cuantities, index=self.crypto , columns=["Cryptos"])
                print(tabulate(aux, headers='keys', tablefmt='pretty'))
                p = "¿Que criptomoneda quieres modificar? "
                ask1 = input(p.rjust(round(self.width / 2) + 5, " "))
                if ask1 in self.crypto:
                    inde = self.crypto.index(ask1)
                    cass = "¿Cantidad adicional? "
                    ask2 = input(cass.rjust(round(self.width / 2) + 5, " "))
                    try:
                        self.cuantities[inde] += float(ask2)
                    except:
                        os.system("cls")
                        for i in range(15):
                            print(self.e)
                        print("Cannot convert to float".center(self.width))
                        time.sleep(5)
                        os.system("cls")
            elif self.ask.lower() == "b":
                self.state = 2
            else:
                self.state = 0
                
    def customize_old(self):
        self.state = 3
        while self.state != 0 and self.state != 2:
            self.state = 3
            os.system("cls")
            self.p_table()
            j = "Escriba la fecha de los datos a modificar siguiedo el formato YYYY-MM-DD, pulse b para volver atrás y enter para salir de la app"
            v = input(j.rjust(round(self.width / 2) + 5, " ") + ": ")
            if v in self.record.index:
                part = self.record.loc[v]
                print(self.e)
                print(self.e)
                v1 = "ad"
                while v1.lower() != "f":
                    os.system("cls")
                    self.p_table()
                    print("DATOS NO ACTUALIZADOS".center(self.width))
                    print(self.e)
                    j = "Modificar (g)astos, (i)ngresos, (t)raspaso, (a)horro o (f)inalizar"
                    v1 = input(j.rjust(round(self.width / 2) + 5, " ") + ": ")
                    if v1.lower() == "g":
                        print(self.e)
                        j = "Inserte cantidad adicional de gasto1, si no inserta nada o inserta un elemento no convertible a float se mantendra la actual"
                        continue_ = True
                        v2 = input(j.rjust(round(self.width / 2) + 5, " ") + ": ")
                        try:
                            float(v2)
                        except:
                            continue_ = False
                        if continue_:
                            print(self.e)
                            pr = "Capital de (b)anco o (g)asto, si no inserta nada o un valor no válido no se añadirá el dato: "
                            h1 = input(pr.rjust(round(self.width / 2) + 5, " "))
                            if h1.lower() == "b":
                                part["Capital bancario"] -= float(v2)
                                part["Gastos1"] += float(v2)
                            if h1.lower() == "g":
                                part["Capital gasto"] -= float(v2)
                                part["Gastos1"] += float(v2)
                            print(self.e)
                            if h1.lower() == "b" or h1.lower() =="g":
                                j = "Concepto, si no añade nada se ajustará como Indefinido: "
                                v3 = input(j.rjust(round(self.width / 2) + 5, " ") + ": ")
                                if v3.strip() != "":
                                    part["Concepto1"] = v3
                                else: 
                                    part["Concepto1"] = "Indefinido"
                        print(self.e)

                        j = "Inserte cantidad adicional de gasto2, si no inserta nada o inserta un elemento no convertible a float se mantendra la actual"
                        continue_ = True
                        v2 = input(j.rjust(round(self.width / 2) + 5, " ") + ": ")
                        try:
                            float(v2)
                        except:
                            continue_ = False
                        if continue_:
                            print(self.e)
                            pr = "Capital de (b)anco o (g)asto, si no inserta nada o un valor no válido no se añadirá el dato: "
                            h1 = input(pr.rjust(round(self.width / 2) + 5, " "))
                            if h1.lower() == "b":
                                part["Capital bancario"] -= float(v2)
                                part["Gastos2"] += float(v2)
                            if h1.lower() == "g":
                                part["Capital gasto"] -= float(v2)
                                part["Gastos2"] += float(v2) 
                            print(self.e)
                            if h1.lower() == "b" or h1.lower() =="g":
                                j = "Concepto, si no añade nada se ajustará como Indefinido: "
                                v3 = input(j.rjust(round(self.width / 2) + 5, " ") + ": ")
                                if v3.strip() != "":
                                    part["Concepto2"] = v3
                                else: 
                                    part["Concepto2"] = "Indefinido"
                        print(self.e)

                        j = "Inserte cantidad adicional de gasto3, si no inserta nada o inserta un elemento no convertible a float se mantendra la actual"
                        continue_ = True
                        v2 = input(j.rjust(round(self.width / 2) + 5, " ") + ": ")
                        try:
                            float(v2)
                        except:
                            continue_ = False
                        if continue_:
                            print(self.e)
                            pr = "Capital de (b)anco o (g)asto, si no inserta nada o un valor no válido no se añadirá el dato: "
                            h1 = input(pr.rjust(round(self.width / 2) + 5, " "))
                            if h1.lower() == "b":
                                part["Capital bancario"] -= float(v2)
                                part["Gastos3"] += float(v2)
                            if h1.lower() == "g":
                                part["Capital gasto"] -= float(v2)
                                part["Gastos3"] += float(v2)
                            print(self.e)
                            if h1.lower() == "b" or h1.lower() =="g":
                                j = "Concepto, si no añade nada se ajustará como Indefinido: "
                                v3 = input(j.rjust(round(self.width / 2) + 5, " ") + ": ")
                                if v3.strip() != "":
                                    part["Concepto3"] = v3
                                else: 
                                    part["Concepto3"] = "Indefinido"
                        os.system("cls")
                    elif v1.lower() == "i":
                        j = "Inserte cantidad adicional de Ingreso1, si no inserta nada o inserta un elemento no convertible a float se mantendra la actual"
                        continue_ = True
                        v2 = input(j.rjust(round(self.width / 2) + 5, " ") + ": ")
                        try:
                            float(v2)
                        except:
                            continue_ = False
                        if continue_:
                            print(self.e)
                            pr = "Porcentaje a Capital de Banco si no inserta nada o un valor no válido no se añadirá el dato: "
                            continue__ = True
                            h1 = input(pr.rjust(round(self.width / 2) + 5, " "))
                            try:
                                h1 = float(h1)
                            except:
                                continue__ = False
                            if continue__:
                                if h1 < 100 and h1 > 0:
                                    banco = h1/100
                                    gasto = 1 - banco
                                    part["Capital bancario"] += float(v2) * banco
                                    part["Ingresos1"] += float(v2)
                                    part["Capital gasto"] += float(v2) * gasto
                                    print(self.e)
                                    j = "Concepto, si no añade nada se ajustará como Indefinido: "
                                    v3 = input(j.rjust(round(self.width / 2) + 5, " ") + ": ")
                                    if v3.strip() != "":
                                        part["Concepto_1"] = v3
                                    else: 
                                        part["Concepto_1"] = "Indefinido"
                        print(self.e)

                        j = "Inserte cantidad adicional de Ingreso2, si no inserta nada o inserta un elemento no convertible a float se mantendra la actual"
                        continue_ = True
                        v2 = input(j.rjust(round(self.width / 2) + 5, " ") + ": ")
                        try:
                            float(v2)
                        except:
                            continue_ = False
                        if continue_:
                            print(self.e)
                            pr = "Porcentaje a Capital de Banco si no inserta nada o un valor no válido no se añadirá el dato: "
                            continue__ = True
                            h1 = input(pr.rjust(round(self.width / 2) + 5, " "))
                            try:
                                h1 = float(h1)
                            except:
                                continue__ = False
                            if continue__:
                                
                                if h1 < 100 and h1 > 0:
                                    banco = h1/100
                                    gasto = 1 - banco
                                    part["Capital bancario"] += float(v2) * banco
                                    part["Ingresos2"] += float(v2)
                                    part["Capital gasto"] += float(v2) * gasto
                                    print(self.e)
                                    j = "Concepto, si no añade nada se ajustará como Indefinido: "
                                    v3 = input(j.rjust(round(self.width / 2) + 5, " ") + ": ")
                                    if v3.strip() != "":
                                        part["Concepto_2"] = v3
                                    else: 
                                        part["Concepto_2"] = "Indefinido"
                        os.system("cls")
                    elif v1.lower() == "t":
                        print(self.e)
                        j = "Inserte la descripción del Traspaso, si no se inserta nada o un valor no válido (Válidos: Banco a gasto [b a g], al reves [g a b], respete las minúsculas) no se realizará"
                        v2 = input(j.rjust(round(self.width / 2) + 5, " ") + ": ")
                        if v2.strip() != "" and (v2.strip() == "b a g" or v2.strip() == "g a b"):
                            part["Descripción"] = v2
                            print(self.e)
                            j = "Inserte la cantidad"
                            continue_ = True
                            v3 = input(j.rjust(round(self.width / 2) + 5, " ") + ": ")
                            try:
                                part["Traspasos"] += float(v2)
                            except: 
                                continue_ = False
                            if continue_:
                                if v2 == "b a g":
                                    part["Capital bancario"] -= float(v3)
                                    part["Capital gasto"] += float(v3)
                                else:
                                    part["Capital bancario"] += float(v3)
                                    part["Capital gasto"] -= float(v3)
                        os.system("cls")
                    elif v1.lower() == "a":
                        print(self.e)
                        j = "Inserte la cantidad adicional"
                        continue_ = True
                        v2 = input(j.rjust(round(self.width / 2) + 5, " ") + ": ")
                        try:
                            float(v2)
                        except:
                            continue_ = False
                        if continue_:
                            part["Ahorro"] += float(v2)
                            part["Capital bancario"] -= float(v2)
                            part["Capital ahorrado"] += float(v2)
                        os.system("cls")
                    else:
                        v1 = "f"
                

                partition = self.record.loc[v:]
                dcb = part["Capital bancario"] - self.record["Capital bancario"].loc[v]
                dcg = part["Capital gasto"] - self.record["Capital gasto"].loc[v]
                dca = part["Capital ahorrado"] - self.record["Capital ahorrado"].loc[v]
                partition["Capital bancario"] += dcb
                partition["Capital gasto"] += dcg
                partition["Capital ahorrado"] += dca
                partition.loc[v] = part
                self.record.loc[v:] = partition  
                os.system("cls")  
            elif v.lower() == "b":
                self.state = 2
            elif v.strip() == "":
                self.state = 0        
                
    def customize_new(self):
        self.status = 3
        while self.status != 2 and self.status != 0:
            self.status = 3
            os.system("cls")
            self.opciones(["Crear nueva semana"])
            v = input(self.o.rjust(round(self.width / 2) + 5, " ") + ": ")
            if v.lower() == "a":
                delta = np.timedelta64(1, 'W')
                day = np.datetime64(self.record.index[-1], "D") + delta
                capitalb = self.record["Capital bancario"].iloc[-1]
                capitalg = self.record["Capital gasto"].iloc[-1]
                capitala = self.record["Capital ahorrado"].iloc[-1]
                C = pd.concat([self.record.Concepto1, self.record.Concepto2, self.record.Concepto3]).to_numpy()
                C = pd.DataFrame(np.unique(C), columns=["Gastos"])
                G = pd.concat([self.record.Concepto_1, self.record.Concepto_2]).to_numpy()
                G = pd.DataFrame(np.unique(G), columns=["Ingresos"])
                G = tabulate(G, headers='keys', tablefmt='pretty')
                print(tabulate(C, headers='keys', tablefmt='pretty'))
                print(G.ljust(round(self.width / 2) + 5, " "))
                for i in range(10):
                    print(self.e)
                c = []
                for i in range(len(self.record.columns)):
                    if i != 0 and c[i - 1] == "":
                        c.append(0)
                        continue
                    j = self.record.columns[i]
                    v1 = input(j.rjust(round(self.width / 2) + 5, " ") + ": ")
                    if self.record[j].dtype == "string":
                        c.append(v1.strip())
                    else:
                        if v1 == "":
                            v1 = 0
                        try:
                            if float(v1) != float(0):
                                if i < 11:
                                    if i < 6:
                                        pr = "b o g: "
                                        v2 = input(pr.rjust(round(self.width / 2) + 5, " "))
                                        if v2.lower() == "b":
                                            capitalb -= float(v1)
                                        elif v2.lower() == "g":
                                            capitalg -= float(v1)
                                        else:
                                            c[i-1] = ""
                                    else:
                                        pr = "banco: "
                                        v2 = input(pr.rjust(round(self.width / 2) + 5, " "))
                                        try:
                                            capitalb += float(v2)
                                        except:
                                            c[i-1] = ""
                                        pr = "gasto: "
                                        v2 = input(pr.rjust(round(self.width / 2) + 5, " "))
                                        try:
                                            capitalg += float(v2)
                                        except: 
                                            c[i-1] = ""
                                elif i == 11:
                                    if c[i - 1] == "b a g":
                                        capitalb -= float(v1)
                                        capitalg += float(v1)
                                    elif c[i - 1] == "g a b":
                                        capitalg -= float(v1)
                                        capitalb += float(v1)
                                    else:
                                        c[i-1] = ""
                                c.append(float(v1))
                                if j == "Ahorro":
                                    capitalb -= float(v1)
                                    capitala += float(v1)
                                    break
                        except:
                            c.append(float(0))
                            if j != "Ahorro":
                                c[i-1] = ""
                            else:
                                break
                
                c.append(capitalb)
                c.append(capitalg)
                c.append(capitala)
                self.record.loc[day] = c
                os.system("cls")
            elif v.lower() == "b":
                self.status = 2
            else:
                self.status = 0
                            
    def customize(self):
        self.state = 2
        while self.state != 1 and self.state != 0:
            self.state = 2
            if self.options_data["Crypto"]:
                self.opciones(["Nueva Semana", "Semana Anterior", "Cryptos"])
            else:
                self.opciones(["Nueva Semana", "Semana Anterior"])
            self.ask = input(self.o.rjust(round(self.width / 2) + 5, " "))
            os.system("cls")
            if self.ask.lower() == "a":
                self.customize_new()
                os.system("cls")
            elif self.ask.lower() == "b":
                self.customize_old()
                os.system("cls")
            elif self.ask.lower() == "c":
                if self.options_data["Crypto"]:
                    self.customize_cryptos()
                    os.system("cls")
                else:
                    self.state = 1
            elif self.ask.lower() == "d":
                if self.options_data["Crypto"]:
                    self.state = 1
                else:
                    self.state = 0
            else:
                self.state = 0
        self.rounddf()

    def view(self):
        self.state = 2
        while self.state != 0 and self.state != 1:
            self.state = 2
            self.p_table()
            self.opciones(["Vista Detallada"], 1)
            self.ask = input(self.o.rjust(round(self.width / 2) + 5, " "))
            if self.ask.lower() == "a":
                print(self.e)
                j = "Insert a week (YYY-MM-DD) or a couple of weeks (, separator not space), or a range of weeks (_ separator): "
                j1 = input(j.rjust(round(self.width / 2) + 15))
                os.system("cls")
                if j1 in self.record.index:
                    os.system("cls")
                    print(tabulate(pd.DataFrame(self.record.loc[j1]), headers='keys', tablefmt='pretty'))
                    for _ in range(15):
                        print(self.e)
                    input(self.oli.rjust(round(self.width / 2) + 15))
                    os.system("cls")
                elif "_" in j1:
                    j1 = j1.split("_")
                    os.system("cls")
                    if j1[0] in self.record.index and j[1] in self.record.index:
                        print(tabulate(self.record.loc[j1[0]:j1[1]], headers='keys', tablefmt='pretty'))
                        for _ in range(15):
                            print(self.e)
                        input(self.oli.rjust(round(self.width / 2) + 15))
                        os.system("cls")
                elif "," in j1:
                    j1 = j1.split(",")
                    os.system("cls")
                    condition = True
                    for _ in j1:
                        if not _ in self.record.index:
                            condition = False
                    if condition:
                        print(tabulate(self.record.loc[j1], headers='keys', tablefmt='pretty'))
                        for _ in range(15):
                            print(self.e)
                        input(self.oli.rjust(round(self.width / 2) + 15))
                        os.system("cls")
            elif self.ask.lower() == "b":
                self.state = 1
                os.system("cls")
            else:
                self.state = 0
                os.system("cls")

    def conceptos(self):
        self.state = 3
        while self.state != 0 and self.state != 2:
            self.state = 3
            C = pd.concat([self.record.Concepto1, self.record.Concepto2, self.record.Concepto3]).to_numpy()
            G = pd.concat([self.record.Gastos1, self.record.Gastos2, self.record.Gastos3]).to_numpy()
            SM = pd.DataFrame([], columns=["Gastos Totales", "Media de Gasto", "Desviación Típica", "Media Semanal", "Porcentaje del Total"], index=np.unique(C))
            for i in np.unique(C):
                SM["Gastos Totales"].loc[i] = round(G[C == i].sum(), 2)
                SM["Media de Gasto"].loc[i] = round(G[C == i].mean(), 2)
                SM["Desviación Típica"].loc[i] = round(G[C == i].std(), 2)
                SM["Media Semanal"].loc[i] = round(G[C == i].sum() / self.record.shape[0], 2)
                SM["Porcentaje del Total"].loc[i] =  round((G[C == i].sum() / G.sum()) * 100, 2)
            SM = SM[SM["Gastos Totales"] != 0.00]
            C1 = pd.concat([self.record.Concepto_1, self.record.Concepto_2]).to_numpy()
            I = pd.concat([self.record.Ingresos1, self.record.Ingresos2]).to_numpy()
            SM1 = pd.DataFrame([], columns=["Ingresos Totales", "Media de Ingresos", "Desviación Típica", "Media Semanal", "Porcentaje del Total"], index=np.unique(C1))
            for i in np.unique(C1):
                SM1["Ingresos Totales"].loc[i] = round(I[C1 == i].sum(), 2)
                SM1["Media de Ingresos"].loc[i] = round(I[C1 == i].mean(), 2)
                SM1["Desviación Típica"].loc[i] = round(I[C1 == i].std(), 2)
                SM1["Media Semanal"].loc[i] = round(I[C1 == i].sum() / self.record.shape[0], 2)
                SM1["Porcentaje del Total"].loc[i] =  round((I[C1 == i].sum() / I.sum()) * 100, 2)
            SM1= SM1[SM1["Ingresos Totales"] != 0.00]           
            self.opciones(["Datos", "Gráfica"])
            self.ask = input(self.o.rjust(round(self.width / 2) + 5, " "))
            os.system("cls")
            if self.ask.lower() == "a":
                SM = SM.sort_values(by=["Gastos Totales"], ascending=False)
                print(tabulate(SM, headers='keys', tablefmt='pretty'))
                SM1 = SM1.sort_values(by=["Ingresos Totales"], ascending=False)
                print(tabulate(SM1, headers='keys', tablefmt='pretty'))
                for i in range(15):
                    print(self.e)
                input(self.oli.rjust(round(self.width / 2) + 15))
                os.system("cls")
            elif self.ask == "b":
                figure, (ax1, ax2) = plt.subplots(1, 2)
                ax1.pie(SM["Gastos Totales"],  labels=SM.index, shadow=True, autopct='%1.1f%%', startangle=90)
                ax1.axis('equal')
                ax1.title.set_text("Gastos Totales")
                ax2.pie(SM1["Ingresos Totales"],  labels=SM1.index, shadow=True, autopct='%1.1f%%', startangle=90)
                ax2.axis('equal')
                ax2.title.set_text("Ingresos Totales")
                figure.show()
                for _ in range(15):
                    print(self.e)
                input(self.oli.rjust(round(self.width / 2) + 15))
                os.system("cls")
            elif self.ask == "c":
                self.state = 2
            else:
                self.state = 0

    def g_i(self):
        self.state = 3
        while self.state != 0 and self.state != 2:
            self.state = 3
            GS = self.record.Gastos1 + self.record.Gastos2 + self.record.Gastos3
            IS = self.record.Ingresos1 + self.record.Ingresos2
            BS = IS - GS
            combined_max = max([max(GS), max(IS), max(BS), self.options_data["maxG"]])
            combined_min = min([min(GS), min(IS), min(BS)])
            os.system("cls")
            self.opciones(["Datos", "Gráfica"])
            self.ask = input(self.o.rjust(round(self.width / 2) + 5, " "))
            os.system("cls")
            if self.ask.lower() == "a":
                df = pd.DataFrame([])
                df["Gastos Totales"] = GS.round(2)
                df["Ingresos Totales"] = IS.round(2)
                df["Beneficios totales"] = BS.round(2)
                metrics = pd.DataFrame(columns=["Gastos", "Ingresos", "Beneficios"], index=["Total", "Media", "Desviación Típica"])
                metrics["Gastos"].iloc[0] = round(GS.sum(), 2)
                metrics["Ingresos"].iloc[0] = round(IS.sum(), 2)
                metrics["Beneficios"].iloc[0] = round(BS.sum(), 2)
                metrics["Gastos"].iloc[1] = round(GS.mean(), 2)
                metrics["Ingresos"].iloc[1] = round(IS.mean(), 2)
                metrics["Beneficios"].iloc[1] = round(BS.mean(), 2)
                metrics["Gastos"].iloc[2] = round(GS.std(), 2)
                metrics["Ingresos"].iloc[2] = round(IS.std(), 2)
                metrics["Beneficios"].iloc[2] = round(BS.std(), 2)
                print(tabulate(df, headers='keys', tablefmt='pretty'))
                print(tabulate(metrics, headers='keys', tablefmt='pretty'))
                for _ in range(5):
                    print(self.e)
                input(self.oli.rjust(round(self.width / 2) + 15))
            elif self.ask == "b":
                fig = plt.figure()
                gd = gridspec.GridSpec(2,3)
                ax1 = fig.add_subplot(gd[0,:])
                ax1.plot(GS.index, GS, label="Gastos Totales")
                ax1.plot(IS.index, IS, label="Ingresos Totales")
                ax1.plot(BS.index, BS, label="Benficios Totales" )
                ax1.plot(GS.index, self.options_data["maxG"] * np.ones(len(GS.index)), label="Objetivo de Gasto")
                ax1.set_ylabel("Euros")
                ax1.set_xlabel("Tiempo")
                ax1.legend()
                ax1.grid()
                ax2 = fig.add_subplot(gd[1,0])
                ax2.hist(GS, GS.shape[0])
                ax2.set_title("Histograma Gastos")
                ax3 = fig.add_subplot(gd[1,1])
                ax3.hist(IS, IS.shape[0])
                ax3.set_title("Histograma Ingresos")
                ax4 = fig.add_subplot(gd[1,2])
                ax4.hist(BS, BS.shape[0])
                ax4.set_title("Histograma Beneficios")
                

                if self.options_data["Axis"] == 3:
                    ax1.set_xticks(GS.index, rotation="vertical")
                    t = np.linspace(combined_min, combined_max, 20, dtype="int").tolist()
                    t.append(0)
                    ax1.set_yticks(t)
                    
                    t1 = np.linspace(0, GS.shape[0], 20, dtype="int").tolist()
                    ax2.set_yticks(t1)
                    
                    t2 = np.linspace(0, IS.shape[0], 20, dtype="int").tolist()
                    ax3.set_yticks(t2)
                    
                    t3 = np.linspace(0, BS.shape[0], 20, dtype="int").tolist()
                    ax4.set_yticks(t3)
                elif self.options_data["Axis"] == 2:
                    ax1.set_xticks(GS.index[::2], rotation="vertical")
                    t = np.linspace(combined_min, combined_max, 10, dtype="int").tolist()
                    t.append(0)
                    ax1.set_yticks(t)
                    
                    t1 = np.linspace(0, GS.shape[0], 10, dtype="int").tolist()
                    ax2.set_yticks(t1)
                    
                    t2 = np.linspace(0, IS.shape[0], 10, dtype="int").tolist()
                    ax3.set_yticks(t2)
                    
                    t3 = np.linspace(0, BS.shape[0], 10, dtype="int").tolist()
                    ax4.set_yticks(t3)
                else:
                    ax1.set_xticks(GS.index[::4])
                    t = np.linspace(combined_min, combined_max, 5, dtype="int").tolist()
                    t.append(0)
                    ax1.set_yticks(t)
                    
                    t1 = np.linspace(0, GS.shape[0], 5, dtype="int").tolist()
                    ax2.set_yticks(t1)
                    
                    t2 = np.linspace(0, IS.shape[0], 5, dtype="int").tolist()
                    ax3.set_yticks(t2)
                    
                    t3 = np.linspace(0, BS.shape[0], 5, dtype="int").tolist()
                    ax4.set_yticks(t3)
                fig.show()
                for _ in range(15):
                    print(self.e)
                input(self.oli.rjust(round(self.width / 2) + 15))
            elif self.ask == "c":
                self.state = 2
            else:
                self.state = 0

    def capitales(self):
        self.init_patrimonio()
        self.state = 3
        while self.state != 0 and self.state != 2:
            self.state = 3
            os.system("cls")
            self.opciones(["Datos", "Gráfica"])
            self.ask = input(self.o.rjust(round(self.width / 2) + 5, " "))
            os.system("cls")
            j = self.record[["Capital bancario", "Capital gasto", "Capital ahorrado"]]
            j["Capital Disponible"] = j["Capital bancario"] + j["Capital gasto"]
            j["Capital Disponible"] = j["Capital Disponible"].astype("float").round(2)
            j["Capital Total"] = j["Capital Disponible"] + j["Capital ahorrado"]
            j["Capital Total"] = j["Capital Total"].astype("float").round(2)
            if self.ask.lower() == "a":
                print(tabulate(pd.DataFrame(j), headers='keys', tablefmt='pretty'))
                if self.options_data["Crypto"]:
                    self.actual_patrimonio()
                    print(tabulate(self.patrimonio, headers='keys', tablefmt='pretty'))
                for i in range(15):
                    print(self.e)
                input(self.oli.rjust(round(self.width / 2) + 15))
            elif self.ask.lower() == "b":
                if self.options_data["Crypto"]:
                    self.actual_patrimonio()
                    figure, (ax1, ax2) = plt.subplots(2, 1)
                    p1 = list(self.crypto)
                    p1.append("Euros")
                    ax1.pie(self.patrimonio[p1].iloc[1],  labels=p1, shadow=True, autopct='%1.1f%%', startangle=90)
                    ax1.axis('equal')
                    ax1.title.set_text(" Distribución Patrimonio")
                    for i in j.columns:
                        ax2.plot(j.index, j[i], label=i)
                    ax2.grid()
                    ax2.legend()
                    ax2.set_ylabel("Euros")
                    ax2.set_xlabel("Tiempo")
                    if self.options_data["Axis"] == 3:
                        ax2.set_xticks(j.index)
                        ax2.set_yticks(np.linspace(min(j.min()), max(j.max()), 20, dtype="int"))
                    elif self.options_data["Axis"] == 2:
                        ax2.set_xticks(j.index[::2])
                        ax2.set_yticks(np.linspace(min(j.min()), max(j.max()), 10, dtype="int"))
                    else:
                        ax2.set_xticks(j.index[::4])
                        ax2.set_yticks(np.linspace(min(j.min()), max(j.max()), 5, dtype="int"))
                    ax2.title.set_text("Seguimiento Capitales")
                    figure.show()
                else:
                    for i in j.columns:
                        plt.plot(j.index, j[i], label=i)
                    plt.grid()
                    plt.legend()
                    plt.ylabel("Euros")
                    plt.xlabel("Tiempo")
                    if self.options_data["Axis"] == 3:
                        plt.xticks(j.index)
                        plt.yticks(np.linspace(min(j.min()), max(j.max()), 20, dtype="int"))
                    elif self.options_data["Axis"] == 2:
                        plt.xticks(j.index[::2])
                        plt.yticks(np.linspace(min(j.min()), max(j.max()), 10, dtype="int"))
                    else:
                        plt.xticks(j.index[::4])
                        plt.yticks(np.linspace(min(j.min()), max(j.max()), 5, dtype="int"))
                    plt.title("Seguimiento de Capitales")
                    plt.show()
                    
            elif self.ask.lower() == "c":
                self.state = 2
            else:
                self.state = 0

    def metrics(self):
        os.system("cls")
        self.state = 2
        while self.state != 0 and self.state != 1:
            self.state = 2
            self.opciones(["Conceptos", "Gastos e Ingresos", " Cápitales"])
            self.ask = input(self.o.rjust(round(self.width / 2) + 5, " "))
            os.system("cls")
            if self.ask.lower() == "a":
                self.conceptos()
            elif self.ask.lower() == "b":
                self.g_i()
            elif self.ask.lower() == "c":
                self.capitales()
            elif self.ask.lower() == "d":
                self.state = 1
            else:
                self.state = 0

    def p_table(self):
        p = [self.g, self.g, self.e, tabulate(self.record, headers='keys', tablefmt='pretty'), self.e, self.g, self.g,
             self.e, self.e, self.e]
        for i in p:
            print(i)

    def main_page(self):
        self.state = 1
        self.p_title()
        self.opciones(["Ver Estado", "Agregar Datos", "Obtener Métricas", "Configuración"], 7, False)
        self.ask = input(self.o.rjust(round(self.width / 2) + 5, " "))
        os.system("cls")

    def p_title(self):
        tg = "---------------------------------------------------------------------------------------------------------------------------------------------------------------------"
        t1 = "####### ### ###  ##  ####### ###  ##   ###### ###  ####### ###        ######   #####  ###  ### ###  ## #########     ##### ###  ###   ##### ######### ####### ##   ##"
        t2 = "##      ### #### ##  ##   ## #### ##  ###     ###  ##   ## ###       ###      ##   ## ###  ### #### ##    ###       ###    ###  ###  ###       ###    ##      ### ###"
        t3 = "####### ### #######  ####### #######  ###     ###  ####### ###       ###      ##   ## ###  ### #######    ###       ###    ########  ###       ###    ####### #######"
        t4 = "##      ### ### ###  ##   ## ### ###  ###     ###  ##   ## ###       ###      ##   ## ###  ### ### ###    ###       ###      ###     ###       ###    ###     ## # ##"
        t5 = "##      ### ###  ##  ##   ## ###  ##   ###### ###  ##   ## #######    ######   #####    ####   ###  ##    ###    #####       ###  #####        ###    ####### ##   ##"
        ts = [tg, tg, self.e, t1, t2, t3, t4, t5, self.e, tg, tg, self.e, self.e, self.e]
        for i in ts:
            print(i.center(self.width))

    def init_patrimonio(self):
        if self.options_data["Crypto"]: 
            self.crypto = ["ada", "btc", "rose", "agix", "adax"]
            urls = ["https://coinmarketcap.com/es/currencies/cardano/", "https://coinmarketcap.com/es/currencies/bitcoin/",
                    "https://coinmarketcap.com/es/currencies/oasis-network/",
                    "https://coinmarketcap.com/es/currencies/singularitynet/",
                    "https://coinmarketcap.com/es/currencies/adax/"]
            crypt_capital = []
            prices = []
            for cnt, ur in zip(self.cuantities, urls):
                c = requests.get(ur)
                soup = BeautifulSoup(c.content, "html.parser")
                b = soup.find(class_="priceValue").text.strip()
                b = b[1:]
                price = float(b.replace(",", ""))
                prices.append(price)
                crypt_capital.append(price * cnt * self.deur)
            self.patrimonio = pd.DataFrame(columns=self.crypto, index=["Cantidad", "Euros", "Dólares"])
            self.patrimonio.loc["Cantidad"] = self.cuantities
            self.patrimonio.loc["Euros"] = np.round(np.array(crypt_capital), 2)
            self.patrimonio.loc["Dólares"] = np.round(np.array(crypt_capital)/self.deur, 2)
        else:
            self.patrimonio = pd.DataFrame(index=["Euros", "Dólares"])
    
    def actual_patrimonio(self):
        insertion = [self.record["Capital gasto"].iloc[-1] + self.record["Capital bancario"].iloc[-1] + self.record["Capital ahorrado"].iloc[-1],0]
        insertion[1] = insertion[0]
        insertion.append(round(insertion[0]/self.deur, 2))
        self.patrimonio["Cryptos"] = [1, round(self.patrimonio.loc["Euros"].sum(), 2), round(self.patrimonio.loc["Dólares"].sum(), 2)]
        self.patrimonio["Euros"] = insertion
        self.patrimonio["Patrimonio"] = [1, round(self.patrimonio["Cryptos"].loc["Euros"] + self.patrimonio["Euros"].loc["Euros"]) , round(self.patrimonio["Cryptos"].loc["Dólares"] + self.patrimonio["Euros"].loc["Dólares"])]

    def check_progress(self):
        os.system("cls")
        for _ in range(50):
            print(self.e)
        w = "Save Data?"
        print(w.center(self.width))
        print(self.e)
        w = "Y or N: "
        t = input(w.rjust(round(self.width / 2)))
        if t.lower() == "y":
            self.rounddf()
            self.record = self.record.convert_dtypes()
            self.record.to_pickle("record.pkl")
            np.save("cuantities.npy", self.cuantities)
        os.system("cls")

    def outro(self):
        os.system("cls")
        for _ in range(15):
            print(self.e)
        t = [".----------------.  .----------------.  .----------------.  .----------------.   .----------------.  .----------------.  .----------------.  .-----------------. .----------------.  .----------------.",
        "| .--------------. || .--------------. || .--------------. || .--------------. | | .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |",
        "| |   ______     | || |  ____  ____  | || |  _________   | || |              | | | |  _________   | || |  ____  ____  | || |      __      | || | ____  _____  | || |  ___  ____   | || |    _______   | |",
        "| |  |_   _ \    | || | |_  _||_  _| | || | |_   ___  |  | || |              | | | | |  _   _  |  | || | |_   ||   _| | || |     /  \     | || ||_   \|_   _| | || | |_  ||_  _|  | || |   /  ___  |  | |",
        "| |    | |_) |   | || |   \ \  / /   | || |   | |_  \_|  | || |              | | | | |_/ | | \_|  | || |   | |__| |   | || |    / /\ \    | || |  |   \ | |   | || |   | |_/ /    | || |  |  (__ \_|  | |",
        "| |    |  __'.   | || |    \ \/ /    | || |   |  _|  _   | || |              | | | |     | |      | || |   |  __  |   | || |   / ____ \   | || |  | |\ \| |   | || |   |  __'.    | || |   '.___`-.   | |",
        "| |   _| |__) |  | || |    _|  |_    | || |  _| |___/ |  | || |      _       | | | |    _| |_     | || |  _| |  | |_  | || | _/ /    \ \_ | || | _| |_\   |_  | || |  _| |  \ \_  | || |  |`\____) |  | |",
        "| |  |_______/   | || |   |______|   | || | |_________|  | || |     )_/      | | | |   |_____|    | || | |____||____| | || ||____|  |____|| || ||_____|\____| | || | |____||____| | || |  |_______.'  | |",
        "| |              | || |              | || |              | || |              | | | |              | || |              | || |              | || |              | || |              | || |              | |",
        "| '--------------' || '--------------' || '--------------' || '--------------' | | '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |",
        "'----------------'  '----------------'  '----------------'  '----------------'   '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'"]
        for i in t:
            print(i.center(self.width))
        time.sleep(2)
        os.system("cls")

    def run(self):
        self.init_patrimonio()
        while self.state != 0:
            self.main_page()
            if self.ask.lower() == "a":
                self.view()
            elif self.ask.lower() == "b":
                self.customize()
            elif self.ask.lower() == "c":
                self.metrics()
            elif self.ask.lower() == "d":
                self.options()
            else:
                self.state = 0
            if self.state == 0:
                if self.confirm():
                    self.state = 0
                else:
                    self.state = -1
        self.check_progress()
        self.outro()
        keyboard.press("f11")
