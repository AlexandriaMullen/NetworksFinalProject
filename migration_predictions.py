#https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html
from sklearn.linear_model import LogisticRegression as lr
#https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html
from sklearn.neighbors import KNeighborsClassifier as knn
#dealing with the excel file:
#https://datatofish.com/read_excel/
import pandas as pd
import tkinter as tk
from tkinter import filedialog

print('import complete')

def input_data():
    #this excel file, 'UN_MigrantStockTotal_2017' has 8 tabs
    #each saying slightly different things about the same data

    root = tk.Tk()
    canvas1 = tk.Canvas(root, width = 300, height = 300, bg = 'lightsteelblue')
    canvas1.pack()

    getExcel()

    browseButton_Excel = tk.Button(text='Import Excel File', command=getExcel, bg='green', fg='white', font=('helvetica', 12, 'bold'))
    canvas1.create_window(150, 150, window=browseButton_Excel)

    root.mainloop()

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
    print(df)
    
def knn_migration(data):
    return None

def lr_migration(data):
    return None
