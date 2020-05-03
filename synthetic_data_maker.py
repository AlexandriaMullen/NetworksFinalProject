import numpy as np

#we'll allow the sythetic data to vary between +15 and -15 percent up and down
variation_percetage = 0.15

def make_new_data(Xs,Ys):

    new_Xs = Xs.copy()
    new_Ys = Ys.copy()

    for dp_index in range(len(Xs)):
        num_migs = Ys[dp_index]
        abs_val_migrants = (variation_percetage * num_migs) #num migrants up or down
        #want 100 more normally distributed datapoints per year:
        #low = num_migs[dp_index] - abs_val_migrants
        #high = num_migs[dp_index] + abs_val_migrants

        if(num_migs == 0):
            print("number of imms is 0, breaking program")
            break
        
        ys = []
        ys = list(np.random.normal(loc = num_migs,
                       scale = abs_val_migrants,
                       size = 100))
        
        #give them an x (i.e. year) value
        #low = X[dp_index][0] + 0.01
        #high = X[dp_index][0] + 0.99
        
        xs = []
        xs = list(np.random.normal(loc = Xs[dp_index][0] +.5,
                                   scale = .25,
                                   size = 100))

        for i in range(len(xs)):
            new_Ys.append(ys[i])
            new_Xs.append([xs[i]])

    #print(Ys,Xs)

    #print(synth_x[0],synth_y)
    return [new_Ys,new_Xs]
        
