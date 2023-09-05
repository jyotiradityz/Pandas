import pandas as pd
s1=pd.Series(25,index=[1,2,3,4,4,5,6])
s2=pd.Series(5,index=[1,2,3,4])
print(s1+s2)