import pandas as pd
l={"a":[1,2,3,4],"b":[12,32,435,54]}

var=pd.DataFrame(l)

#insertion
var.insert(1,"Python",[4,5,6,2])


#update

var["Python"]=var['a'][:3]

#deletion

var.pop('Python')
del var['a']
var