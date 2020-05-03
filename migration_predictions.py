#https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html
from sklearn.linear_model import LogisticRegression as lr
#https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsRegressor.html
from sklearn.neighbors import KNeighborsRegressor as knn

def knn_migration(x_train,y_train,x_test,y_test):
    #FIT AND PREDICT:
    neigh = knn(n_neighbors = 3)
    neigh.fit(x_train,y_train)
    
    print("Accuraccy: ", neigh.score(x_test,y_test))
    
    input_year = input("What year would you like to predict?\nYear must be after 2013\n")
    input_year = int(input_year)

    pred = neigh.predict([[input_year]])

    print(pred)    
    
    return input_year,pred

def lr_migration(x_train,y_train,x_test,y_test):
    #FIT AND PREDICT:
    clf = lr(random_state = 0,
             #solver = lbfgs,
             #multi_class = auto
             ).fit(x_train,y_train)
    
    print("Accuraccy: ", clf.score(x_test,y_test))
    
    input_year = input("What year would you like to predict?\nYear must be after 2013\n")
    input_year = int(input_year)

    pred = clf.predict([[input_year]])
    
    print(pred)
    
    return input_year,pred
