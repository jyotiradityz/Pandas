import pandas as pd

dic={"name":['python','c','c++','go'],
     "por":[1,2,3,4],
     "rank":[1,3,2,4]}

var1=pd.DataFrame(dic)
print(var1)


#column

var2=pd.DataFrame(dic,columns=['name'])

print(var2)

#indexChange

var3=pd.DataFrame(dic,columns=['name','por'],index=['a','b','v',12])
print(var3)


#using Series

d={"a":pd.Series([1,2,3,4]),"b":pd.Series([1,2,3,4])}

ans=pd.DataFrame(d)

print(ans)