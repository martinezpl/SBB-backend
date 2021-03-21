import pandas as pd
import json

data = pd.read_pickle('data/complete_sbb_data.pkl').dropna()
a = []
b = []
c = []
facers = set(data['facility'])
for facility in facers:
    a.append(data.loc[data['facility'] == facility, 'facility_id'].values[0])
    b.append(data.loc[data['facility'] == facility, 'traffic'].values[0])
    c.append(data.loc[data['facility'] == facility, 'max_spots'].values[0])

keyer = {q: [w, e, r] for q, w, e, r in zip(
    facers, a, b , c)}

with open('facilities.json', 'w') as outfile:
    json.dump(keyer, outfile)
