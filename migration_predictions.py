#https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html
from sklearn.linear_model import LogisticRegression as lr
#https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsRegressor.html
from sklearn.neighbors import KNeighborsRegressor as knn
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


