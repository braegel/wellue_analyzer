import sys
import pandas as pd

df=pd.read_csv(sys.argv[1])
print ("Median Bloodpressure: %d/%d" % (df['SYS(mmHg)'].median(),df['DIA(mmHg)'].median()))
