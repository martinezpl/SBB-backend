import os
import datetime
from tensorflow import keras
import pandas as pd
import numpy as np
import pickle
import json 

class Logic():
    def __init__(self):
        with open('pickle_model.pkl', 'rb') as file:
            pickle_model = pickle.load(file)
        
        json_model = keras.models.load_model('model.json')
        self.model = json_model
        with open('facilities.json') as json_file:
            self.data = json.load(json_file)

    def _prepare_data(self, facility, date):
        print("DATE:", date)
        facility_id, traffic, max_spots = self.data[facility]
        date = date.split('-')
        yr = date[0]
        m = date[1]
        d = date[2]
        h = date[3]
        time = pd.to_datetime(f"{yr}/{m}/{d}T{h}:00:00+00:00")
        wd = time.weekday()
        weekend = (lambda x: 0 if x < 5 else 1)(wd)
        return np.asarray(pd.Series({'weekend': weekend, 'weekday': wd, 'hour': h, 'month': m, 'day': d, 'facility_id': facility_id, 'traffic': traffic, 'max_spots': max_spots})).reshape(1, -1).astype('float32')
        
    def pred(self, facility, date):
        X = self._prepare_data(facility, date)
        pred = self.model.predict(X)
        return int(np.argmax(pred[0]))

    def detail(self, facility, date):
        # do konca dnia predykcje preds double
        facility = facility[0].capitalize() + facility[1:]
        preds = []
        d = date.split('-')
        if len(d[3]) < 2:
            date += "0"
        date = date[:-2]
        for i in range(23):
            preds.append(self.pred(facility, date + str(i)))
        return json.dumps({"preds":preds})

    def home(self):
        # facility(str), max_spots(int), taken_pred(int) in json
        json_arr = []
        for fac in self.data.keys():
            _, __, max_spots = self.data[fac]
            json_arr.append({"facility": fac,
                "max_spots": int(max_spots),
                "taken_all": self.pred(fac, datetime.datetime.now().strftime("%Y-%m-%d-%H"))})
        return json.dumps(json_arr)

    def rafcik(self):
        return json.dumps([{
        "facility":"1 nazwa",
        "max_spots":33,
        "taken_all":22
        },
        {
        "facility":"2 nazwa",
        "max_spots":44,
        "taken_all":33
        },
        {
        "facility":"3 nazwa",
        "max_spots":55,
        "taken_all":44
        },
        {
        "facility":"4 nazwa",
        "max_spots":66,
        "taken_all":55
        },
        {
        "facility":"5 nazwa",
        "max_spots":77,
        "taken_all":66
        },
        {
        "facility":"6 nazwa",
        "max_spots":88,
        "taken_all":77
        },
        {
        "facility":"7 nazwa",
        "max_spots":99,
        "taken_all":88
        }]
        )
