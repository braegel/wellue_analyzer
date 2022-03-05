import sys
import pandas as pd

df=pd.read_csv(sys.argv[1])
print ("Median bloodpressure [mmHG]: %d/%d" % (df['SYS(mmHg)'].median(),df['DIA(mmHg)'].median()))
print ("Median heartrate [/s]: %d" % (df['PR(bpm)'].median()))
