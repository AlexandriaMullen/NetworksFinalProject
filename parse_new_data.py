import matplotlib as mp
import numpy as np
import pandas as pd
import tkinter as tk
from tkinter import filedialog

def decide_which_countries():
    global df
    import_file_path = filedialog.askopenfilename()
    xl = pd.ExcelFile(import_file_path)
    df = xl.parse('Totals')
    data = df.to_numpy()
    
    list_of_countries = []
    
    #remove countries with lower data counts
    #i.e. if they don't have any data up to 1985
    for datum in data:
        #test: print(datum),
        for x in range(10):
            #if there's in integer in the first 9 columns
            #keeping in mind the first four are the names of the countries, etc
            #then add that country to the list we'll keep
            if( (isinstance(datum[x], int) or isinstance(datum[x], float))
                and not np.isnan(datum[x])):
                #test: print(datum[x])
                list_of_countries.append(datum[0])
                #no need to check the next four if applicable
                continue

    #kill duplicates:
    list_of_countries = list(set(list_of_countries))

    #print(list_of_countries)

    try:
        list_of_countries.remove('CntName')
    except ValueError:
        print('Wrong File!!')
    
    return list_of_countries

def make_migrant_table(excelPath):
    countries = decide_which_countries()

    data_by_country = []

    for country in countries:

        xl = pd.ExcelFile(excelPath)
        df = xl.parse()
        data = df.to_numpy()

        data_by_country.append([country,data])
                
    
