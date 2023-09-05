import pandas as pd
l={"a":[1,2,3,4],"b":[12,32,435,54]}
var=pd.DataFrame(l)
var['c']=var['a'] if var['a']<=2 else -1
var