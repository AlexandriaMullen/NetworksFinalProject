#https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html
from sklearn.linear_model import LogisticRegression as lr
#https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html
from sklearn.neighbors import KNeighborsClassifier as knn
#dealing with the excel file:
#https://datatofish.com/read_excel/
import pandas as pd
import tkinter as tk
from tkinter import filedialog
import numpy as np

print('import complete')

#opens the window that allows for inportation of excel file,
#imports it
#and cleans it up
def input_data():
    #this excel file, 'UN_MigrantStockTotal_2017' has 8 tabs
    #each saying slightly different things about the same data

    root = tk.Tk()
    canvas1 = tk.Canvas(root, width = 300, height = 300, bg = 'lightsteelblue')
    canvas1.pack()

    #get the data, put it into a numpy array
    #then clean it up (we don't want every row and column, after all)
    data = clean_up_data(getExcel())

    browseButton_Excel = tk.Button(text='Import Excel File', command=getExcel, bg='green', fg='white', font=('helvetica', 12, 'bold'))
    canvas1.create_window(150, 150, window=browseButton_Excel)

    root.mainloop()

    return data

#handling and cleaning up the data:
def clean_up_data(npdf):

    data = []
    
    columns_we_want = [1,5,6,7,8,9,10,11,12]
    rows_we_want =  ( #the -2 accounts for the fact that the row is labelled '30,49',etc but
                      #python calls it 28, etc, etc
                    list(range(30-2,50-2)) + list(range(51-2,60-2)) +
                    list(range(61-2,68-2)) + list(range(69-2,74-2)) +
                    list(range(75-2,92-2)) + list(range(94-2,99-2)) +
                    list(range(100-2,107-2)) + list(range(108-2,117-2)) +
                    list(range(118-2,129-2)) + list(range(130-2,148-2)) +
                    list(range(150-2,160-2)) + list(range(161-2,174-2)) +
                    list(range(175-2,191-2)) + list(range(192-2,201-2)) +
                    list(range(203-2,229-2)) + list(range(230-2,238-2)) +
                    list(range(239-2,253-2)) + list(range(254-2,259-2)) +
                    list(range(261-2,263-2)) + list(range(264-2,269-2)) +
                    list(range(270-2,277-2)) + list(range(278-2,287-2))
                    )
    #test: print(rows_we_want)
    for row in range(len(npdf)):
        if(row not in rows_we_want):
            #skip
            continue
        #print('Row we\'re on: ', row),
        #print('Row contents: ', npdf[row]),
        datum = []
        for column in range(len(npdf[row])):
            if(column not in columns_we_want):
                #skip
                continue
            #print('Row we\'re on: ', column),
            #print('Data point: ', npdf[row][column])

            datum.append(npdf[row][column])
        data.append(datum)
        print(datum)

    print(data)
    return data
            
def getExcel():
    global df
    
    import_file_path = filedialog.askopenfilename()
    #df = pd.read_excel(import_file_path)

    #https://stackoverflow.com/questions/42887663/reading-multiple-tabs-from-excel-in-different-dataframes
    #for our predictions, we're just going to use tab 2 (named table 1)

    xl = pd.ExcelFile(import_file_path)
    #print(xl.sheet_names)
    
    #print (df)

    df = xl.parse(xl.sheet_names[1]) #Getting table 1
    #print(df)
    #https://pythonexamples.org/convert-pandas-dataframe-to-numpy-array/
    data = df.to_numpy()

    return data
    
def knn_migration(data):
    return None

def lr_migration(data):
    return None

input_data()
