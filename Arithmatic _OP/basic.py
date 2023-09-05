import pandas as pd
l={"a":[1,2,3,4],"b":[1,2,3,4]}
var=pd.DataFrame(l)
var["c"]=var["a"]+var["b"]
var["d"]=var["a"]-var["b"]
var["e"]=var["a"]*var["b"]
var["f"]=var["a"]/var["b"]
var