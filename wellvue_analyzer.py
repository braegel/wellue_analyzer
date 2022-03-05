import sys
import pandas as pd

df=pd.read_csv(sys.argv[1])
print(df['SYS(mmHg)'].median())
print(df['DIA(mmHg)'].median())
