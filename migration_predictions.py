#https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html
from sklearn.linear_model import LogisticRegression as lr
#https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html
from sklearn.neighbors import KNeighborsClassifier as knn
#our own code:
import parse_new_data

def knn_migration(x_train,y_train,x_test,y_test):
    neigh = knn(n_neighbors = 3)
    neigh.fit(x_train,y_train)
    
    print("Accuraccy: ", neigh.score(x_test,y_test))
    
    input_year = input("What year would you like to predict?\nYear must be after 2013")
    input_year = int(input_year)

    print(neigh.predict([[input_year]]))    
    return None

def lr_migration(x_train,y_train,x_test,y_test):
    clf = lr(random_state = 0).fit(x_train,y_train)
    
    print("Accuraccy: ", clf.score(x_test,y_test))
    
    input_year = input("What year would you like to predict?\nYear must be after 2013")
    input_year = int(input_year)
    
    print(clf.predict([[input_year]]))
    
    return None

def main(): 
    
    #IDEA:
    #Ask usr for countries
    #gather data,
    #trim, clean up data as necessary
    #push data to ML model
    #make predictions!!
    
    print("These are the following countries:")
    print(parse_new_data.decide_which_countries())
    cnt_to_cnt = input("From which country to which country would you like to predict?\n Input should be typed as \'CountryName to CountryName\'.\n")

    cnts = cnt_to_cnt.split(' ')
    cnts.remove('to')
    print("You have entered:", cnts)

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
