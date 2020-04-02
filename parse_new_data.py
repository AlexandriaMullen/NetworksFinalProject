import matplotlib as mp
import pandas as pd
import tkinter as tk
import numpy as np
from tkinter import filedialog


def decide_which_countries():
    global df
    xl = pd.ExcelFile("./data/UN_MigFlow_Totals.xlsx")
    df = xl.parse('Totals')
    data = df.to_numpy()

    list_of_countries = []

    # remove countries with lower data counts
    # i.e. if they don't have any data up to 1985
    for datum in data:
        # test: print(datum),
        for x in range(10):
            # if there's in integer in the first 9 columns
            # keeping in mind the first four are the names of the countries, etc
            # then add that country to the list we'll keep
            if ((isinstance(datum[x], int) or isinstance(datum[x], float))
                    and not np.isnan(datum[x])):
                # test: print(datum[x])
                if (datum[0] == "United Kingdom of Great Britain and Northern Ireland"):
                    list_of_countries.append(("United Kingdom", datum[1]))
                else:
                    list_of_countries.append((datum[0], datum[1]))
                # no need to check the next four if applicable
                continue

    # kill duplicates:
    list_of_countries = list(set(list_of_countries))

    # print(list_of_countries)

    try:
        list_of_countries.remove(('CntName', 'Criteria'))
    except ValueError:
        print('Wrong File!!')

    return list_of_countries


def make_migrant_table():
    countries = decide_which_countries()

    data_by_country = []

    for country, criteria in countries:

        excelPath = "./data/" + country + ".xlsx"
        xl = pd.ExcelFile(excelPath)
        # we need the Australia, Germany, US, (etc) by Residence tab:
        #but the tab is different for each thing
        print("Country: ", country, "|", end = " ")
        df = None
        try:
            if country == "United States of America":
                df = xl.parse("USA by " + criteria)
            else:
                df = xl.parse(country + " by " + criteria)
        except:
            df = xl.parse("USA by " + criteria) #USA fails sometimes because python string checking sucks

        data = df.to_numpy()

        data = country_data(country, data)

        data_by_country.append(data)

    return data_by_country


# Given string country's name and nparr data
# pick out the important bits
def country_data(country, data):
    new_data = []
    for datum in data:  # data is list of rows
        if (datum[0] == 'Immigrants'):
            row = [datum[2] + 'to ' + country, [datum[9:43]]]  # dub check 42 or 43 (DONE)
            new_data.append(row)
    return new_data
