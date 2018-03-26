import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KernelDensity
from sklearn.grid_search import GridSearchCV
from math import tan, pi
import numpy as np
from colorsys import hsv_to_rgb
import random
from scipy.interpolate import griddata
from scipy.ndimage import zoom


all_2016 = pd.read_csv("C:\\Users\\Austin\\Documents\\Baseball\\savant_data_all_gb.csv").replace('null', np.nan)


out_list = ["Groundout", "Forceout", "Fielders Choice Out", "Grounded Into DP", "Field Error"]
no_count_list = []
columns = ["events", "pitcher", "pitcher_name", "pitch_type", "pitch_id", "hit_angle", "hit_speed"]
hit_list = ["Single", "Double", "Triple"]

singles = 0
doubles = 0
triples = 0
hits = 0
outs = 0

total = 0


hit_vector = all_2016[['events', 'hc_x', 'hc_y', 'hit_speed', 'hit_angle']].dropna()
pd.to_numeric(hit_vector.hc_x)
pd.to_numeric(hit_vector.hc_y)


for index, row in hit_vector.iterrows():
    if row['events'] == 'Single':
        singles += 1
        hits += 1
    elif row['events'] in out_list:
        outs += 1
    elif row['events'] == "Double":
        doubles += 1
        hits += 1
    elif row['events'] == "Triple":
        triples += 1
        hits += 1
    total += 1


def horizontal_angle(x, y):
    return round(tan((x-128)/(208-y))*180/pi*.75, 1)


single_prob = float(singles) / float(total)
double_prob = float(doubles) / float(total)
triple_prob = float(triples) / float(total)
hit_prob = float(hits) / float(total)
out_prob = float(outs) / float(total)

hit_vector['spray_angle'] = map(horizontal_angle, hit_vector['hc_x'], hit_vector['hc_y'])

out_rows = hit_vector.loc[hit_vector['events'].isin(out_list)]
single_rows = hit_vector.loc[hit_vector['events'] == 'Single']
double_rows = hit_vector.loc[hit_vector['events'] == 'Double']
triple_rows = hit_vector.loc[hit_vector['events'] == 'Triple']


hit_vector = hit_vector.drop(hit_vector.columns[[0, 1, 2]], axis=1)
out_rows = out_rows.drop(out_rows.columns[[0, 1, 2]], axis=1)
single_rows = single_rows.drop(single_rows.columns[[0, 1, 2]], axis=1)
double_rows = double_rows.drop(double_rows.columns[[0, 1, 2]], axis=1)
triple_rows = triple_rows.drop(triple_rows.columns[[0, 1, 2]], axis=1)
hit_rows = pd.concat([single_rows, double_rows, triple_rows])


kde = KernelDensity(bandwidth=4.53793103448)
kde2 = KernelDensity(bandwidth=5.5620689655172413)
heat_list = []

## grid = GridSearchCV(KernelDensity(),
                #    {'bandwidth': np.linspace(0.1, 10.0, 30)},
              #      cv=20) # 20-fold cross-validation
## grid.fit(hit_rows)
## print grid.best_params_

# print("best bandwidth: {0}".format(grid.best_estimator_.bandwidth))

kde.fit(hit_vector)
kde2.fit(hit_rows)

for angle in xrange(-20, 5):
    for spray in xrange(-45, 45):
        some_hit = [[93, angle, spray]]

        prob_x = np.exp(kde.score(np.array(some_hit)))
        prob_yup = np.exp(kde2.score(np.array(some_hit)))

        prob_total = prob_yup * hit_prob / prob_x

        heat_list.append(prob_total)


X = np.array([[i for i in range(-45, 45)] for q in range(-20, 5)])
Y = np.array([[i for q in range(-45, 45)] for i in range(-20, 5)])


heat_list = np.array(heat_list)
heat_list = heat_list.reshape(25, 90)

plt.contourf(X, Y, heat_list)
clb = plt.colorbar()
plt.title("Rogers Center hit probability on ground balls")
plt.xlabel('Horizontal angle')
plt.ylabel('Vertical angle')
plt.show()

