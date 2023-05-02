import pandas as pd
import numpy as np
import pickle

df = pd.read_csv('./dataset.csv')

transmission = pd.get_dummies(df['transmission'])
fuel = pd.get_dummies(df['fuel'])
owner = df['owner'].map(lambda x: 1 if x=='First Owner' else 2 if x=='Second Owner' else 3)

X = pd.concat([transmission,fuel,owner,df.drop(['transmission','fuel','owner','selling_price'],axis=1)],axis=1)

my_model = pickle.load(open('./random_forest.pkl', 'rb'))

def predict_price(trans, fuel_type, previous_owner, year, km_driven):

    trans = trans.title()
    fuel_type = fuel_type.title()

    x = []
    x[:8] = np.zeros(8,dtype='int32')
    x[5] = previous_owner
    x[6] = year
    x[7] = km_driven

    transmission_index = np.where(X.columns==trans)[0][0]
    fuel_index = np.where(X.columns==fuel_type)[0][0]
    
    if transmission_index>=0:
        x[transmission_index] = 1
    if fuel_index>=2:
        x[fuel_index] = 1
        
    return float(format(my_model.predict([x])[0],'.2f'))

# print(predict_price('Manual', 'Diesel', 1, 2018, 45000))