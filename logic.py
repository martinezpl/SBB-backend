import sklearn
import datetime
import pandas as pd
import numpy as np
import pickle

def pred(date=0, place=0):
    with open('pickle_model.pkl', 'rb') as file:
        pickle_model = pickle.load(file)
    date = date.split('-')
    yr = date[0]
    m = date[1]
    d = date[2]
    h = date[3]
    time = pd.to_datetime(f"{yr}/{m}/{d}T{h}:00:00+00:00")
    wd = time.weekday()
    weekend = (lambda x: 0 if x < 5 else 1)(wd)
    X = np.array(pd.Series({'weekend': weekend, 'weekday': wd, 'hour': h})).reshape(1, -1)
    pred = round(pickle_model.predict(X)[0], 2)
    return f"{pred}"
