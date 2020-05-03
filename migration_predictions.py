from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
#https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html
from sklearn.linear_model import LogisticRegression as lr
#https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html
from sklearn.neighbors import KNeighborsClassifier as knn
from sklearn.svm import LinearSVC
#our own code:
import parse_new_data

def knn_migration(data):
    return None

def lr_migration(data):
    return None

def linSVM_migration(data):
    return None

plt.figure(figsize=(30,15))
m = Basemap(projection='cyl',
                llcrnrlat = -90,
                llcrnrlon = -180,
                urcrnrlat = 90,
                urcrnrlon = 180,
                resolution='l')
    
def route(a,b):
        x = (lonDict.get(a)+lonDict.get(b))/2
        y = (latDict.get(a)+latDict.get(b))/2
        p = a+" to "+b
        m.drawgreatcircle(lonDict.get(a),latDict.get(a),lonDict.get(b),latDict.get(b),linewidth=4,color='b')
        plt.annotate(p,(x,y),color='w',size=15)
 
m.drawcoastlines()
m.drawcountries(linewidth=2)
plt.title('Routing Cities')
m.bluemarble()
        
def main(): 
    print("These are the following countries:")
    print(parse_new_data.decide_which_countries())
    cnt_to_cnt = input("From which country to which country would you like to predict?\n Input should be typed as \'CountryName to CountryName\'.\n")

    cnts = cnt_to_cnt.split(' ')
    cnts.remove('to')
    print("You have entered:", cnts)
    
        
    latDict = {}
    lonDict={}
    
    with open("latarray.txt") as f:
        for line in f:
            (key, val) = line.split(" : ")
            line = line.strip('\n')
            latDict[key] = float(val)
    with open("longarray.txt") as f:
        for line in f:
            (key, val) = line.split(" : ")
            line = line.strip('\n')
            lonDict[key] = float(val)    
    
    route(cnts[0],cnts[1])
    plt.show()
   
    imm_data = []

    #from parse data:
    data = parse_new_data.make_migrant_table()
    for dest_country in data:
        if(dest_country == cnts[1]):
            print(dest_country)
            for incoming_country in dest_country:
                imm_data = incoming_country[1]
                print(incoming_country)
    print(imm_data)     

    X = [a for a in range(1980,2013)]

    x_train = []
    y_train = []
    x_test = []
    y_test = []
    #split daat up into testing, training;
    #1980-2004 will be training
    #2004-2013 will be testing
    
main()
