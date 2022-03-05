import sys
import pandas as pd
import datetime
import matplotlib.pyplot as plt

print()
df=pd.read_csv(sys.argv[1])

print ("Median bloodpressure [mmHG]: %d/%d" % (df['SYS(mmHg)'].median(),df['DIA(mmHg)'].median()))
print ("Median heartrate [/s]: %d" % (df['PR(bpm)'].median()))
print()

timestamps=[]
for index, row in df.iterrows():
#    print(type(datetime.datetime.strptime(row['DateTime'],"%Y-%m-%d %H:%M:%S")))
    timestamps.append(datetime.datetime.strptime(row['DateTime'],"%Y-%m-%d %H:%M:%S"))
df["timestamp"]=timestamps
#print(df.head())
weeks = [g for n, g in df.groupby(pd.Grouper(key='timestamp',freq='W'))]
#print(type(weeks))
print('Median values per week:')
for week in weeks:
    print("%d\t%d\t%d\t%d" % (week.iloc[0]['timestamp'].isocalendar()[1],week['SYS(mmHg)'].median(),week['DIA(mmHg)'].median(),week['PR(bpm)'].median()))
    # boxplot = week.boxplot(column=['SYS(mmHg)','DIA(mmHg)']);
    # plt.title(week.iloc[0]['timestamp'].isocalendar()[1])
    # plt.show()

boxplot = df.boxplot(column=['SYS(mmHg)','DIA(mmHg)']);
plt.title("Gesamt")
plt.show()
