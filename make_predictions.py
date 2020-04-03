import parse_new_data as pnd

def trim_data(X,imm_data):
    new_imm_data = []
    new_years = []
    for index in range(len(imm_data)):
        if(imm_data[index] == '..'):
            continue
        else:
            new_imm_data.append(imm_data[index])
            new_years.append(X[index])
    return new_imm_data, new_years

def main():
    # IDEA:
    # Ask usr for countries
    # gather data,
    # trim, clean up data as necessary
    # push data to ML model
    # make predictions!!

    print("These are the following countries:")
    countries = pnd.decide_which_countries()
    print(countries)
    cnt_to_cnt = input(
        "From which country to which country would you like to predict?\n Input should be typed as \'CountryName to CountryName\'.\n")

    cnts = cnt_to_cnt.split(' ')
    cnts.remove('to')
    print("You have entered:", cnts)

    imm_data = []

    # from parse data:
    print("Fetching " + country + " ")
    data = pnd.make_migrant_table(countries)
    print("Data fetched.")
    for country_and_immigration_data in data:
        if country_and_immigration_data[0] == cnts[1]:
            print(country_and_immigration_data)
        #    for source_country_and_immigration_data in country_and_immigration_data[1]:
        #       imm_data = incoming_country[1]
        #       print(incoming_country)
    # print(imm_data)

    # X = [a for a in range(1980,2013)]

    x_train = []
    y_train = []
    x_test = []
    y_test = []
    # split data up into testing, training;
    # 1980-2004 will be training
    # 2004-2013 will be testing


main()