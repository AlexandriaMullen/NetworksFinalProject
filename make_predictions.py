import parse_new_data
import migration_predictions
from sklearn.model_selection import train_test_split
from matplotlib import pyplot

def trim_data(X,imm_data):
    new_imm_data = []
    new_years = []
    #print(len(X),",",len(imm_data))
    for index in range(len(imm_data)):
        if(imm_data[index] == '..'):
            continue
        else:
            try:
                new_imm_data.append(float(imm_data[index]))
                #need the extra brackets for the ML model input
                new_years.append([X[index]])
            except IndexError:
                print("Data cleaned.")
    return new_imm_data,new_years

def main():
    # IDEA:
    # Ask usr for countries
    # gather data,
    # trim, clean up data as necessary
    # push data to ML model
    # make predictions!!

    print("These are the following countries:")
    print(parse_new_data.decide_which_countries())
    cnt_to_cnt = input(
        "\n\nFrom which country to which country would you like to predict?\nInput should be typed as \'CountryName to CountryName\'.\n")

    cnts = cnt_to_cnt.split('to')
    #cannot split with spaces, because:
    #problem: this splits up countries like
    #United Kingdom, United States of America, and New Zealand
    #We would need to detect and correct this^
    #now we need to remove the first and last chars b/c they're spaces.
    cnts[0] = cnts[0][:-1]  #remove last character
    cnts[1] = cnts[1][1:]   #remove frst character
    
    print("You have entered:", cnts)
    
    imm_data = []

    # from parse data:
    data = parse_new_data.make_migrant_table()
    for country_and_immigration_data in data:
        #print(country_and_immigration_data[0])
        if (country_and_immigration_data[0] == cnts[1]):
            #print("Yes")
            for imm_country_dat in country_and_immigration_data:
                #print(imm_country_dat)
                for n in range(len(imm_country_dat)):
                    #print(imm_country_dat[n])
                    if(imm_country_dat[n][0] == cnts[0]):
                        #print(imm_country_dat[n][1])
                        imm_data = imm_country_dat[n][1]
    #print(imm_data)

    #We need it to go up to 2013, this is how python range works (ANNOYING)
    X = [a for a in range(1980,2014)]

    imm_data = trim_data(X,imm_data)

    #print(imm_data)

    #X is now imm_data[1], Y is imm_data[0]
    #split data up into testing, training;
    X_train, X_test, y_train, y_test = train_test_split(
        imm_data[1], imm_data[0], test_size=0.25, random_state=0)

    #print(X_train)
    #print(y_train)
    #print(X_test)
    #print(y_test)

    #Time for predictions!
    print("K-Nearest Neighbor Regression model:")
    input_year1,pred1 = migration_predictions.knn_migration(X_train,y_train,X_test,y_test)
    print("Linear Regression model:")
    input_year2,pred2 = migration_predictions.lr_migration(X_train,y_train,X_test,y_test)


    #plot
    new_X = []
    Y = imm_data[0]

    for n in range(len(imm_data[1])):
        new_X.append(imm_data[1][n][0])

    #print(new_X)

    pyplot.plot(new_X,Y, color = 'r', marker = ".")
    prediction1, = pyplot.plot([input_year1],[pred1], color = 'b', label = 'KNN pred', marker = ".")
    prediction2, = pyplot.plot([input_year2],[pred2], color = 'g', label = 'LR  pred', marker = ".")
    pyplot.ylabel("People Per Year")
    pyplot.xlabel("Year")
    pyplot.title("Immigration from " + cnts[0] + " to " + cnts[1] + " with Predictions")
    pyplot.legend(handles = [prediction1,prediction2])
    pyplot.show()
    
    #End of main
    
main()
