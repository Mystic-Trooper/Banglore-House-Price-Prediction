import json
import pickle
import numpy as np
# global variables
__locations= None
__data_columns= None
__model= None

# First Routine
def get_location_names():
    # This should read the columns.json file and return the locations
    # first 3 columns are not location but other fields
    return __locations

# Second Routine
def get_estimated_price(location,sqft,bhk,bath):
    # return predicted price
    try:
        loc_index=__data_columns.index(location.lower())
    except:
        loc_index=-1
    # returns column index for a given location
    x= np.zeros(len(__data_columns))
    # all zeroes
    x[0]= sqft
    x[1]= bath
    x[2]= bhk
    if loc_index >=0:
        x[loc_index]=1
        # set that location index as 1
    # float number to 2 decimal places
    return round(__model.predict([x])[0],2)

def load_saved_artifacts():
    print("Loading the saved Artifacts..... Starts")
    global __data_columns
    global __locations

    with open("server-/artifacts/columns.json",'r') as f:
        __data_columns= json.load(f)['data_columns']
        __locations= __data_columns[3:]
        global __model
    with open("server-/artifacts/banglore_home_prices_model.pickle",'rb') as f:
        __model= pickle.load(f)

    print("loading of artifacts....done")

if __name__=='__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('1st Phase JP Nagar',1000,2,3))
    print(get_estimated_price('1st Phase JP Nagar',1000,2,2))
    print(get_estimated_price('Indira Nagar',1000,3,3))
    print(get_estimated_price('Indira Nagar',2000,2,2))

