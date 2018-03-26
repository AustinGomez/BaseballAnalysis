import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data_fielding_2012 = pd.read_csv("C:\\Users\\Austin\\Documents\\Baseball\\defense_2012.csv").replace("null", "NaN")
data_fielding_2013 = pd.read_csv("C:\\Users\\Austin\\Documents\\Baseball\\defense_2013.csv").replace("null", "NaN")
data_fielding_2014 = pd.read_csv("C:\\Users\\Austin\\Documents\\Baseball\\defense_2014.csv").replace("null", "NaN")
data_fielding_2015 = pd.read_csv("C:\\Users\\Austin\\Documents\\Baseball\\defense_2015.csv").replace("null", "NaN")
data_fielding_2016 = pd.read_csv("C:\\Users\\Austin\\Documents\\Baseball\\defense_2016.csv").replace("null", "NaN")

data_fielding_some = pd.read_csv("C:\\Users\\Austin\\Documents\\Baseball\\savant.csv").replace("null", "NaN")

data_2012_all = pd.read_csv("C:\\Users\\Austin\\Documents\\Baseball\\ground_ball_data_all_2012.csv").replace("null", "NaN")
data_2013_all = pd.read_csv("C:\\Users\\Austin\\Documents\\Baseball\\ground_ball_data_all_2013.csv").replace("null", "NaN")
data_2014_all = pd.read_csv("C:\\Users\\Austin\\Documents\\Baseball\\ground_ball_data_all_2014.csv").replace("null", "NaN")
data_2015_all = pd.read_csv("C:\\Users\\Austin\\Documents\\Baseball\\ground_ball_data_all_2015.csv").replace("null", "NaN")
data_2016_all = pd.read_csv("C:\\Users\\Austin\\Documents\\Baseball\\ground_ball_data_all_2016.csv").replace("null", "NaN")

data_2010 = pd.read_csv("C:\\Users\\Austin\\Documents\\Baseball\\ground_ball_data_2010.csv").replace("null", "NaN")
data_2011 = pd.read_csv("C:\\Users\\Austin\\Documents\\Baseball\\ground_ball_data_2011.csv").replace("null", "NaN")
data_2012 = pd.read_csv("C:\\Users\\Austin\\Documents\\Baseball\\ground_ball_data_2012.csv").replace("null", "NaN")
data_2013 = pd.read_csv("C:\\Users\\Austin\\Documents\\Baseball\\ground_ball_data_2013.csv").replace("null", "NaN")
data_2014 = pd.read_csv("C:\\Users\\Austin\\Documents\\Baseball\\ground_ball_data_2014.csv").replace("null", "NaN")
data_2015 = pd.read_csv("C:\\Users\\Austin\\Documents\\Baseball\\ground_ball_data_2015.csv").replace("null", "NaN")
data_2016 = pd.read_csv("C:\\Users\\Austin\\Documents\\Baseball\\ground_ball_data_2016.csv").replace("null", "NaN")

out_list = ["Groundout", "Forceout", "Fielders Choice Out", "Grounded Into DP"]
no_count_list = ["Field Error"]
columns = ["events", "pitcher", "pitcher_name", "pitch_type", "pitch_id", "hit_angle", "hit_speed"]
hit_list = ["Single", "Double", "Triple"]
raw_fielding_averages = [data_fielding_2012.at[14, "FP"], data_fielding_2013.at[14, "FP"],
                         data_fielding_2014.at[14, "FP"], data_fielding_2015.at[14, "FP"],
                         data_fielding_2016.at[14, "FP"]]
def ground_ball_babip(batted_balls):
    hits = 0
    ab = 0
    bj_hits = 0
    bj_ab = 0
    for index, row in batted_balls.iterrows():
        hits += row["hits"]
        ab += row['abs']
    return float(hits) / float(ab)


hits1 = 0
ab1 = 0
for index, row in data_fielding_some.iterrows():
    if row['events'] in hit_list:
        hits1 += 1
    ab1 += 1


print ground_ball_babip(data_2010)
print ground_ball_babip(data_2011)
print ground_ball_babip(data_2012)
print ground_ball_babip(data_2013)
print ground_ball_babip(data_2014)
print ground_ball_babip(data_2015)
print ground_ball_babip(data_2016)

print ""

print ground_ball_babip(data_2012_all)
print ground_ball_babip(data_2013_all)
print ground_ball_babip(data_2014_all)
print ground_ball_babip(data_2015_all)
print ground_ball_babip(data_2016_all)





