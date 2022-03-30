import numpy as np
import pandas as pd
import os
from tabulate import tabulate
import warnings
import matplotlib.pyplot as plt
import keyboard
import requests
from bs4 import BeautifulSoup
import pickle 


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
        self.k = "1"
        self.o = "Option: "
        self.g = "-".center(self.width, "-")
        warnings.filterwarnings("ignore")
        self.oli = "Press any button to go back "
        self.e = ""
        self.patrimonio = 0
        self.options_data = 0
        self.deur = 0
        self.crypto = 0
        self.options_init()
    
    def options(self):
        pass

    def options_init(self):
        with open("options.pkl", "rb") as op:
            self.options_data = pickle.load(op)

    def rounddf(self):
        self.record["Capital bancario"] = self.record["Capital bancario"].round(2)
        self.record["Capital gasto"] = self.record["Capital gasto"].round(2)
        self.record["Capital ahorrado"] = self.record["Capital ahorrado"].round(2)
        self.record["Gastos1"] = self.record["Gastos1"].round(2)
        self.record["Gastos2"] = self.record["Gastos2"].round(2)
        self.record["Gastos3"] = self.record["Gastos3"].round(2)
        self.record["Ingresos1"] = self.record["Ingresos1"].round(2)
        self.record["Ingresos2"] = self.record["Ingresos2"].round(2)
        self.record["Ahorro"] = self.record["Ahorro"].round(2)
        self.record["Traspasos"] = self.record["Traspasos"].round(2)

    def opciones(self, lista: list, margen: int = 23, condicion=True):
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
            print(m.center(self.width))
            print("".join(l).center(self.width))
            print(" ")
        if condicion:
            m = aux[i + 1] + " - Volver al Inicio"
            print(m.center(self.width))
            print("=   ====== == ======".center(self.width))
            print(" ")
        print("Other - Salir".center(self.width))
        print("=====   =====".center(self.width))
        print(" ")
        print(" ")
        print(" ")

    def customize(self):
        while self.k != 1 and self.k != 0:
            self.opciones(["Nueva Semana", "Semana Anterior"])
            self.k = input(self.o.rjust(round(self.width / 2) + 5, " "))
            os.system("cls")
            if self.k.lower() == "a":
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
                    v = input(j.rjust(round(self.width / 2) + 5, " ") + ": ")
                    if self.record[j].dtype == "string":
                        c.append(v)
                    else:
                        if v == "":
                            v = 0
                        if float(v) != float(0):
                            if i < 11:
                                if i < 6:
                                    pr = "b o g: "
                                    v1 = input(pr.rjust(round(self.width / 2) + 5, " "))
                                    if v1.lower() == "b":
                                        capitalb -= float(v)
                                    if v1.lower() == "g":
                                        capitalg -= float(v)
                                else:
                                    pr = "banco: "
                                    v1 = float(input(pr.rjust(round(self.width / 2) + 5, " ")))
                                    capitalb += v1
                                    pr = "gasto: "
                                    v1 = float(input(pr.rjust(round(self.width / 2) + 5, " ")))
                                    capitalg += v1
                            if i == 11:
                                if c[i - 1] == "b a g":
                                    capitalb -= float(v)
                                    capitalg += float(v)
                                elif c[i - 1] == "g a b":
                                    capitalg -= float(v)
                                    capitalb += float(v)

                        c.append(float(v))
                    if j == "Ahorro":
                        capitalb -= float(v)
                        capitala += float(v)
                        break
                c.append(capitalb)
                c.append(capitalg)
                c.append(capitala)
                self.record.loc[day] = c
                os.system("cls")
            elif self.k.lower() == "b":
                self.p_table()
                j = "Escriba la fecha de los datos a modificar siguiedo el formato YYYY-MM-DD"
                v = input(j.rjust(round(self.width / 2) + 5, " ") + ": ")
                if v in self.record.index:
                    part = self.record.loc[v]
                    print(self.e)
                    print(self.e)
                    j = "Modificar (g)astos, (i)ngresos, (t)raspaso o (a)horro"
                    v1 = input(j.rjust(round(self.width / 2) + 5, " ") + ": ")
                    if v1 == "g" or v1 == "G":
                        print(self.e)
                        j = "Inserte cantidad adicional de gasto1, si no inserta nada se mantendra la actual"
                        v2 = input(j.rjust(round(self.width / 2) + 5, " ") + ": ")
                        if v2 != "":
                            print(self.e)
                            pr = "b o g: "
                            h1 = input(pr.rjust(round(self.width / 2) + 5, " "))
                            if h1.lower() == "b":
                                part["Capital bancario"] -= float(v2)
                            if h1.lower() == "g":
                                part["Capital gasto"] -= float(v2)
                            print(self.e)
                            j = "Concepto"
                            v3 = input(j.rjust(round(self.width / 2) + 5, " ") + ": ")
                            part["Concepto1"] = v3
                            part["Gastos1"] = float(v2) + self.record["Gastos1"].loc[v]
                        print(self.e)
                        j = "Inserte cantidad adicional de gasto2, si no inserta nada se mantendra la actual"
                        v2 = input(j.rjust(round(self.width / 2) + 5, " ") + ": ")
                        if v2 != "":
                            print(self.e)
                            pr = "b o g: "
                            h1 = input(pr.rjust(round(self.width / 2) + 5, " "))
                            if h1.lower() == "b":
                                part["Capital bancario"] -= float(v2)
                            if h1.lower() == "g":
                                part["Capital gasto"] -= float(v2)
                            print(self.e)
                            j = "Concepto"
                            v3 = input(j.rjust(round(self.width / 2) + 5, " ") + ": ")
                            part["Concepto2"] = v3
                            part["Gastos2"] = float(v2) + self.record["Gastos2"].loc[v]
                        print(self.e)
                        j = "Inserte cantidad adicional de gasto3, si no inserta nada se mantendra la actual"
                        v2 = input(j.rjust(round(self.width / 2) + 5, " ") + ": ")
                        if v2 != "":
                            print(self.e)
                            pr = "b o g: "
                            h1 = input(pr.rjust(round(self.width / 2) + 5, " "))
                            if h1.lower() == "b":
                                part["Capital bancario"] -= float(v2)
                            if h1.lower() == "g":
                                part["Capital gasto"] -= float(v2)
                            print(self.e)
                            j = "Concepto"
                            v3 = input(j.rjust(round(self.width / 2) + 5, " ") + ": ")
                            part["Concepto3"] = v3
                            part["Gastos3"] = float(v2) + self.record["Gastos3"].loc[v]
                        os.system("cls")
                    elif v1 == "i" or v1 == "I":
                        print(self.e)
                        j = "Inserte cantidad de Ingreso1, si no inserta nada se mantendra la actual"
                        v2 = input(j.rjust(round(self.width / 2) + 5, " ") + ": ")
                        if v2 != "":
                            print(self.e)
                            pr = "banco: "
                            h1 = float(input(pr.rjust(round(self.width / 2) + 5, " ")))
                            part["Capital bancario"] += h1
                            pr = "gasto: "
                            h1 = float(input(pr.rjust(round(self.width / 2) + 5, " ")))
                            part["Capital gasto"] += h1
                            print(self.e)
                            j = "Concepto"
                            v3 = input(j.rjust(round(self.width / 2) + 5, " ") + ": ")
                            part["Concepto_1"] = v3
                            part["Ingresos1"] = float(v2) + self.record["Ingresos1"].loc[v]
                        print(self.e)
                        j = "Inserte cantidad de Ingreso2, si no inserta nada se mantendra la actual"
                        v2 = input(j.rjust(round(self.width / 2) + 5, " ") + ": ")
                        if v2 != "":
                            print(self.e)
                            pr = "banco: "
                            h1 = float(input(pr.rjust(round(self.width / 2) + 5, " ")))
                            part["Capital bancario"] += h1
                            pr = "gasto: "
                            h1 = float(input(pr.rjust(round(self.width / 2) + 5, " ")))
                            part["Capital gasto"] += h1
                            print(self.e)
                            j = "Concepto"
                            v3 = input(j.rjust(round(self.width / 2) + 5, " ") + ": ")
                            part["Concepto_2"] = v3
                            part["Ingresos2"] = float(v2) + self.record["Ingresos2"].loc[v]
                        os.system("cls")
                    elif v1 == "t" or v1 == "T":
                        print(self.e)
                        j = "Inserte la descripción"
                        v2 = input(j.rjust(round(self.width / 2) + 5, " ") + ": ")
                        if v2 == "b a g" or v2 == "g a b":
                            part["Descripción"] = v2
                            print(self.e)
                            j = "Inserte la cantidad"
                            v3 = input(j.rjust(round(self.width / 2) + 5, " ") + ": ")
                            part["Traspasos"] = float(v2) + self.record["Traspasos"].loc[v]
                            if v2 == "b a g":
                                part["Capital bancario"] -= float(v3)
                                part["Capital gasto"] += float(v3)
                            else:
                                part["Capital bancario"] += float(v3)
                                part["Capital gasto"] -= float(v3)
                        os.system("cls")
                    elif v1 == "a" or v1 == "A":
                        print(self.e)
                        j = "Inserte la cantidad adicional"
                        v2 = input(j.rjust(round(self.width / 2) + 5, " ") + ": ")
                        part["Ahorro"] = float(v2) + self.record["Ahorro"].loc[v]
                        part["Capital bancario"] -= float(v2)
                        part["Capital ahorrado"] += float(v2)
                        os.system("cls")

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
            elif self.k.lower() == "c":
                self.k = 1
            else:
                self.k = 0

    def view(self):
        while self.k != 0 and self.k != 1:
            self.p_table()
            self.opciones(["Vista Detallada"], 1)
            self.k = input(self.o.rjust(round(self.width / 2) + 5, " "))
            if self.k.lower() == "a":
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
                    print(tabulate(self.record.loc[j1[0]:j1[1]], headers='keys', tablefmt='pretty'))
                    for _ in range(15):
                        print(self.e)
                    input(self.oli.rjust(round(self.width / 2) + 15))
                    os.system("cls")
                elif "," in j1:
                    j1 = j1.split(",")
                    os.system("cls")
                    print(tabulate(self.record.loc[j1], headers='keys', tablefmt='pretty'))
                    for _ in range(15):
                        print(self.e)
                    input(self.oli.rjust(round(self.width / 2) + 15))
                    os.system("cls")
            elif self.k.lower() == "b":
                self.k = 1
                os.system("cls")
            else:
                self.k = 0
                os.system("cls")

    def conceptos(self):
        while self.k != 0 and self.k != 1:
            C = pd.concat([self.record.Concepto1, self.record.Concepto2, self.record.Concepto3]).to_numpy()
            G = pd.concat([self.record.Gastos1, self.record.Gastos2, self.record.Gastos3]).to_numpy()
            SM = pd.DataFrame([], columns=["Gastos Totales", "Media de Gasto", "Desviación Típica", "Media Semanal", "Porcentaje del Total"], index=np.unique(C))
            for i in np.unique(C):
                SM["Gastos Totales"].loc[i] = round(G[C == i].sum(), 2)
                SM["Media de Gasto"].loc[i] = round(G[C == i].mean(), 2)
                SM["Desviación Típica"].loc[i] = round(G[C == i].std(), 2)
                SM["Media Semanal"].loc[i] = round(G[C == i].sum() / len(C), 2)
                SM["Porcentaje del Total"].loc[i] =  round((G[C == i].sum() / G.sum()) * 100, 2)
            SM = SM[SM["Gastos Totales"] != 0.00]
            C1 = pd.concat([self.record.Concepto_1, self.record.Concepto_2]).to_numpy()
            I = pd.concat([self.record.Ingresos1, self.record.Ingresos2]).to_numpy()
            SM1 = pd.DataFrame([], columns=["Ingresos Totales", "Media de Ingresos", "Desviación Típica", "Media Semanal", "Porcentaje del Total"], index=np.unique(C1))
            for i in np.unique(C1):
                SM1["Ingresos Totales"].loc[i] = round(I[C1 == i].sum(), 2)
                SM1["Media de Ingresos"].loc[i] = round(I[C1 == i].mean(), 2)
                SM1["Desviación Típica"].loc[i] = round(I[C1 == i].std(), 2)
                SM1["Media Semanal"].loc[i] = round(I[C1 == i].sum() / len(C1), 2)
                SM1["Porcentaje del Total"].loc[i] =  round((I[C1 == i].sum() / I.sum()) * 100, 2)
            SM1= SM1[SM1["Ingresos Totales"] != 0.00]           
            self.opciones(["Datos", "Gráfica"])
            self.k = input(self.o.rjust(round(self.width / 2) + 5, " "))
            os.system("cls")
            if self.k.lower() == "a":
                print(tabulate(SM, headers='keys', tablefmt='pretty'))
                print(tabulate(SM1, headers='keys', tablefmt='pretty'))
                for i in range(15):
                    print(self.e)
                input(self.oli.rjust(round(self.width / 2) + 15))
                os.system("cls")
            elif self.k == "b":
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
            elif self.k == "c":
                self.k = 1
            else:
                self.k = 0

    def g_i(self):
        while self.k != 0 and self.k != 1:
            GS = self.record.Gastos1 + self.record.Gastos2 + self.record.Gastos3
            IS = self.record.Ingresos1 + self.record.Ingresos2
            BS = IS - GS
            os.system("cls")
            self.opciones(["Datos", "Gráfica"])
            self.k = input(self.o.rjust(round(self.width / 2) + 5, " "))
            os.system("cls")
            if self.k.lower() == "a":
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
            elif self.k == "b":
                plt.plot(GS.index, GS, label="Gastos Totales")
                plt.plot(IS.index, IS, label="Ingresos Totales")
                plt.plot(BS.index, BS, label="Benficios Totales" )
                plt.legend()
                plt.grid()
                plt.xticks(GS.index, rotation="vertical")
                plt.show()
                for _ in range(15):
                    print(self.e)
                input(self.oli.rjust(round(self.width / 2) + 15))
            elif self.k == "c":
                self.k = 1
            else:
                self.k = 0

    def capitales(self):
        while self.k != 0 and self.k != 1:
            os.system("cls")
            self.opciones(["Datos", "Gráfica"])
            self.k = input(self.o.rjust(round(self.width / 2) + 5, " "))
            os.system("cls")
            j = self.record[["Capital bancario", "Capital gasto", "Capital ahorrado"]]
            j["Capital Disponible"] = j["Capital bancario"] + j["Capital gasto"]
            if self.k.lower() == "a":
                self.actual_patrimonio()
                print(tabulate(pd.DataFrame(j), headers='keys', tablefmt='pretty'))
                print(tabulate(self.patrimonio, headers='keys', tablefmt='pretty'))
                for i in range(15):
                    print(self.e)
                input(self.oli.rjust(round(self.width / 2) + 15))
            elif self.k.lower() == "b":
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
                ax2.set_xticks(j.index)
                ax2.title.set_text("Seguimiento Capitales")
                figure.show()
            elif self.k.lower() == "c":
                self.k = 1
            else:
                self.k = 0

    def metrics(self):
        os.system("cls")
        while self.k != 0 and self.k != 1:
            self.opciones(["Conceptos", "Gastos e Ingresos", " Cápitales"])
            self.k = input(self.o.rjust(round(self.width / 2) + 5, " "))
            os.system("cls")
            if self.k.lower() == "a":
                self.conceptos()
            elif self.k.lower() == "b":
                self.g_i()
            elif self.k.lower() == "c":
                self.capitales()
            elif self.k.lower() == "d":
                self.k = 1
            else:
                self.k = 0

    def p_table(self):
        p = [self.g, self.g, self.e, tabulate(self.record, headers='keys', tablefmt='pretty'), self.e, self.g, self.g,
             self.e, self.e, self.e]
        for i in p:
            print(i)

    def main_page(self):
        self.init_patrimonio()
        self.p_title()
        self.opciones(["Ver Estado", "Agregar Datos", "Obtener Métricas", "Configuración"], 7, False)
        self.k = input(self.o.rjust(round(self.width / 2) + 5, " "))
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
        iri = "https://www.coingecko.com/es/monedas/tether/eur"
        req = requests.get(iri)
        sr = BeautifulSoup(req.content, "html.parser")
        m = sr.find("span", class_="no-wrap").text
        m = m[1:]
        self.deur = float(m.replace(",", "."))
        cuantities = [223.39, 0.003598, 336.66, 300, 111]
        self.crypto = ["ada", "btc", "rose", "agix", "adax"]
        urls = ["https://coinmarketcap.com/es/currencies/cardano/", "https://coinmarketcap.com/es/currencies/bitcoin/",
                "https://coinmarketcap.com/es/currencies/oasis-network/",
                "https://coinmarketcap.com/es/currencies/singularitynet/",
                "https://coinmarketcap.com/es/currencies/adax/"]
        crypt_capital = []
        prices = []
        for cnt, ur in zip(cuantities, urls):
            c = requests.get(ur)
            soup = BeautifulSoup(c.content, "html.parser")
            b = soup.find(class_="priceValue").text.strip()
            b = b[1:]
            price = float(b.replace(",", ""))
            prices.append(price)
            crypt_capital.append(price * cnt * self.deur)
        self.patrimonio = pd.DataFrame(columns=self.crypto, index=["Cantidad", "Euros", "Dólares"])
        self.patrimonio.loc["Cantidad"] = cuantities
        self.patrimonio.loc["Euros"] = np.round(np.array(crypt_capital), 2)
        self.patrimonio.loc["Dólares"] = np.round(np.array(crypt_capital)/self.deur, 2)
    
    def actual_patrimonio(self):
        insertion = [self.record["Capital gasto"].iloc[-1] + self.record["Capital bancario"].iloc[-1] + self.record["Capital ahorrado"].iloc[-1],0]
        insertion[1] = insertion[0]
        insertion.append(round(insertion[0]/self.deur, 2))
        self.patrimonio["Cryptos"] = [1, round(self.patrimonio.loc["Euros"].sum(), 2), round(self.patrimonio.loc["Dólares"].sum(), 2)]
        self.patrimonio["Euros"] = insertion
        self.patrimonio["Patrimonio"] = [1, self.patrimonio["Cryptos"].loc["Euros"] + self.patrimonio["Euros"].loc["Euros"] , self.patrimonio["Cryptos"].loc["Dólares"] + self.patrimonio["Euros"].loc["Dólares"]]

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
        os.system("cls")

    def run(self):
        while self.k != 0:
            self.main_page()
            if self.k.lower() == "a":
                self.view()
            elif self.k.lower() == "b":
                self.customize()
            elif self.k.lower() == "c":
                self.metrics()
            elif self.k.lower() == "d":
                self.options()
            else:
                self.k = 0
        self.check_progress()
        keyboard.press("f11")
