import pandas as pd
import matplotlib.pyplot as plt




away2008 = pd.read_csv("C:\\Users\\Austin\\Documents\\Baseball\\ground_ball_dataa_2008.csv").replace("null", "NaN")
away2009 = pd.read_csv("C:\\Users\\Austin\\Documents\\Baseball\\ground_ball_dataa_2009.csv").replace("null", "NaN")
away2010 = pd.read_csv("C:\\Users\\Austin\\Documents\\Baseball\\ground_ball_dataa_2010.csv").replace("null", "NaN")
away2011 = pd.read_csv("C:\\Users\\Austin\\Documents\\Baseball\\ground_ball_dataa_2011.csv").replace("null", "NaN")
away2012 = pd.read_csv("C:\\Users\\Austin\\Documents\\Baseball\\ground_ball_dataa_2012.csv").replace("null", "NaN")
away2013 = pd.read_csv("C:\\Users\\Austin\\Documents\\Baseball\\ground_ball_dataa_2013.csv").replace("null", "NaN")
away2014 = pd.read_csv("C:\\Users\\Austin\\Documents\\Baseball\\ground_ball_dataa_2014.csv").replace("null", "NaN")
away2015 = pd.read_csv("C:\\Users\\Austin\\Documents\\Baseball\\ground_ball_dataa_2015.csv").replace("null", "NaN")
away2016 = pd.read_csv("C:\\Users\\Austin\\Documents\\Baseball\\ground_ball_dataa_2016.csv").replace("null", "NaN")

home2008 = pd.read_csv("C:\\Users\\Austin\\Documents\\Baseball\\ground_ball_datah_2008.csv").replace("null", "NaN")
home2009 = pd.read_csv("C:\\Users\\Austin\\Documents\\Baseball\\ground_ball_datah_2009.csv").replace("null", "NaN")
home2010 = pd.read_csv("C:\\Users\\Austin\\Documents\\Baseball\\ground_ball_datah_2010.csv").replace("null", "NaN")
home2011 = pd.read_csv("C:\\Users\\Austin\\Documents\\Baseball\\ground_ball_datah_2011.csv").replace("null", "NaN")
home2012 = pd.read_csv("C:\\Users\\Austin\\Documents\\Baseball\\ground_ball_datah_2012.csv").replace("null", "NaN")
home2013 = pd.read_csv("C:\\Users\\Austin\\Documents\\Baseball\\ground_ball_datah_2013.csv").replace("null", "NaN")
home2014 = pd.read_csv("C:\\Users\\Austin\\Documents\\Baseball\\ground_ball_datah_2014.csv").replace("null", "NaN")
home2015 = pd.read_csv("C:\\Users\\Austin\\Documents\\Baseball\\ground_ball_datah_2015.csv").replace("null", "NaN")
home2016 = pd.read_csv("C:\\Users\\Austin\\Documents\\Baseball\\ground_ball_datah_2016.csv").replace("null", "NaN")

out_list = ["Groundout", "Forceout", "Fielders Choice Out", "Grounded Into DP"]
no_count_list = ["Field Error"]
columns = ["events", "pitcher", "pitcher_name", "pitch_type", "pitch_id", "hit_angle", "hit_speed"]
hit_list = ["Single", "Double", "Triple"]

def ground_ball_babip(batted_balls):
    hits = 0
    ab = 0

    for index, row in batted_balls.iterrows():
        hits += row["hits"]
        ab += row['abs']
    return float(hits) / float(ab)


print str(ground_ball_babip(home2016)) + "      2016 grass"
print ground_ball_babip(away2016)
print ""
print str(ground_ball_babip(home2015)) + "      2015 new turf"
print ground_ball_babip(away2015)
print ""
print str(ground_ball_babip(home2014)) + "      2014 old turf"
print ground_ball_babip(away2014)
print ""
print str(ground_ball_babip(home2013)) + "      2013 old turf"
print ground_ball_babip(away2013)
print ""
print str(ground_ball_babip(home2012)) + "      2012 old turf   new lights"
print ground_ball_babip(away2012)
print ""
print str(ground_ball_babip(home2011)) + "      2011 old turf    old lights"
print ground_ball_babip(away2011)
print ""
print str(ground_ball_babip(home2010)) + "      2010 old turf   old lights"
print ground_ball_babip(away2010)
print ""
print str(ground_ball_babip(home2009)) + "      2009 old turf   old lights"
print ground_ball_babip(away2009)
print ""
print str(ground_ball_babip(home2008)) + "      2008 old turf   old lights"
print ground_ball_babip(away2008)

home = [ground_ball_babip(home2008), ground_ball_babip(home2009), ground_ball_babip(home2010),
        ground_ball_babip(home2011), ground_ball_babip(home2012), ground_ball_babip(home2013),
        ground_ball_babip(home2014), ground_ball_babip(home2015), ground_ball_babip(home2016)]

away = [ground_ball_babip(away2008), ground_ball_babip(away2009), ground_ball_babip(away2010),
        ground_ball_babip(away2011), ground_ball_babip(away2012), ground_ball_babip(away2013),
        ground_ball_babip(away2014), ground_ball_babip(away2015), ground_ball_babip(away2016)]

home_annotate = [ground_ball_babip(home2010), ground_ball_babip(home2011), ground_ball_babip(home2012),
                    ground_ball_babip(home2015), ground_ball_babip(home2016)]


tableau20 = [(31, 119, 180), (174, 199, 232), (255, 127, 14), (255, 187, 120),
             (44, 160, 44), (152, 223, 138), (214, 39, 40), (255, 152, 150),
             (148, 103, 189), (197, 176, 213), (140, 86, 75), (196, 156, 148),
             (227, 119, 194), (247, 182, 210), (127, 127, 127), (199, 199, 199),
             (188, 189, 34), (219, 219, 141), (23, 190, 207), (158, 218, 229)]

for i in range(len(tableau20)):
    r, g, b = tableau20[i]
    tableau20[i] = (r / 255., g / 255., b / 255.)

x_axis = range(2008, 2017)
x_axis_annotate = [2010, 2011, 2012, 2015, 2016]


labels = ["AstroTurf 3D installed", "New lights partially installed", "New lights fully installed", "AstroTurf 3D Xtreme Installed", "Dirt infield installed"]

plt.figure(figsize=(12, 9))
plt.title("BABIP on ground balls")
plt.plot(x_axis, home, lw=2.5, color=tableau20[0])
plt.plot(x_axis, away, lw=2.5, color=tableau20[1])

ax = plt.subplot(111)
ax.spines["top"].set_visible(False)
ax.spines["bottom"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)
plt.xticks(x_axis, x_axis, rotation=45)

y_pos = home[-1]
plt.text(2016.25, y_pos, "Home", fontsize=14, color=tableau20[0])

y_pos = away[-1]
plt.text(2016.25, y_pos, "Away", fontsize=14, color=tableau20[1])

plt.tick_params(top="off", labelbottom="on", right="off", labelleft="on")


for i, txt in enumerate(labels):
    ax.annotate(
        txt,
        (x_axis_annotate[i], home_annotate[i]),
        xytext=(-20, 20),
        textcoords='offset points', ha='right', va='bottom',
        bbox=dict(boxstyle='round,pad=0.3', alpha=0.5),
        arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0'))

plt.show()




