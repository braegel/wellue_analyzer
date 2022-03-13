import sys
import pandas as pd
import datetime
import matplotlib.pyplot as plt

def hypertension_grading(sys,dia):
    sysgrading=-1
    diasgrading=-1
    grading=-1
    # Source https://academic.oup.com/eurheartj/article/39/33/3021/5079119?login=false
    # 2018 ESC/ESH Guidelines for the management of arterial hypertension: The Task Force for the management of arterial hypertension of the European Society of Cardiology (ESC) and the European Society of Hypertension (ESH)
    if sys < 120:
        sysgrading=0
    if sys >= 120 and sys <= 129:
        sysgrading=1
    if sys >= 130 and sys <= 139:
        sysgrading=2
    if sys >= 140 and sys <= 159:
        sysgrading=3
    if sys >= 160 and sys <= 179:
        sysgrading=4
    if sys >= 180:
        sysgrading=5
    if dia < 80:
        diagrading=0
    if dia >= 80 and dia <= 84:
        diagrading=1
    if dia >= 85 and dia <= 89:
        diagrading=2
    if dia >= 90 and dia <= 99:
        diagrading=3
    if dia >= 100 and dia <= 109:
        diagrading=4
    if dia >= 110:
        diagrading=5
    grading=max(sysgrading,diagrading)
    if sys < 120 and dia < 80:
        grading = 0
    if sys >= 140 and dia < 90:
        grading = 6
    return grading

def grading_description(grading):
    description="Undefined"
    if grading == 0:
        description="Optimal"
    if grading == 1:
        description="Normal"
    if grading == 2:
        description="High normal"
    if grading == 3:
        description="Grade 1 hypertension"
    if grading == 4:
        description="Grade 2 hypertension"
    if grading == 5:
        description="Grade 3 hypertension"
    if grading == 6:
        description="Isolated systolic hypertension"
    return(description)
print()
df=pd.read_csv(sys.argv[1])

print ("Median bloodpressure [mmHG]: %d/%d %s" % (df['SYS(mmHg)'].median(),df['DIA(mmHg)'].median(),grading_description(hypertension_grading(df['SYS(mmHg)'].median(),df['DIA(mmHg)'].median()))))
print ("Median heartrate [/s]: %d" % (df['PR(bpm)'].median()))
print()

timestamps=[]
gradings=[]
for index, row in df.iterrows():
#    print(type(datetime.datetime.strptime(row['DateTime'],"%Y-%m-%d %H:%M:%S")))
    timestamps.append(datetime.datetime.strptime(row['DateTime'],"%Y-%m-%d %H:%M:%S"))
    grading=hypertension_grading(row['SYS(mmHg)'],row['DIA(mmHg)'])
    gradings.append(grading)
df["timestamp"]=timestamps
df["grading"]=gradings
#print(df.head())
weeks = [g for n, g in df.groupby(pd.Grouper(key='timestamp',freq='W'))]
#print(type(weeks))
print('Median values per week:')
print('Week\tSys\tDia\tBPM\tN\tGrading')
for week in weeks:
    print("%d\t%d\t%d\t%d\t%i\t%s\tMax: %s" % (week.iloc[0]['timestamp'].isocalendar()[1],week['SYS(mmHg)'].median(),week['DIA(mmHg)'].median(),week['PR(bpm)'].median(),len(week),grading_description(hypertension_grading(week['SYS(mmHg)'].median(),week['DIA(mmHg)'].median())),grading_description(week['grading'].max())))

print()
print('Hypertension Timestamps')

hypertension = df[df['grading'] > 2]
print(hypertension[['DateTime','SYS(mmHg)','DIA(mmHg)','PR(bpm)','grading']].to_string())

    
    # boxplot = week.boxplot(column=['SYS(mmHg)','DIA(mmHg)']);
    # plt.title(week.iloc[0]['timestamp'].isocalendar()[1])
    # plt.show()

boxplot = df.boxplot(column=['SYS(mmHg)','DIA(mmHg)']);
plt.title("Gesamt")
#plt.show()
