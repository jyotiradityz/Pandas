import pandas as pd
dic={"name":['python','c','c++','go'],
     "por":[1,2,3,4],
     "rank":[1,3,2,4]}
ans=pd.Series(dic)
print(ans)