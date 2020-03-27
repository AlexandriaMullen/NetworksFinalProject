#https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html
from sklearn.linear_model import LogisticRegression as lr
#https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html
from sklearn.neighbors import KNeighborsClassifier as knn
from sklearn.svm import LinearSVC
from imblearn.over_sampling import SMOTE
#my own code:
from parse_data import input_data

def knn_migration(data):
    return None

def lr_migration(data):
    return None

def linSVM_migration(data):
    return None

def main():
    #from parse data:
    data = input_data()

    #split daat up into testing, training;
    #1990-2000 will be training
    #2010-2017 will be testing

main()
