import numpy as np
import pandas as pd
from pandas import Series, DataFrame

obj_1 = pd.Series([2, 4, 6])
def check_1():
    print(obj)
    print(obj.values)
    print(obj.index)
obj_2=pd.Series([4,6,10],index=["a","b","c"])
def check_2():
    print(obj_2)
    print(obj_2.index)
    print(obj_2["b"])
    print(obj_2[["c","a"]])
    print(obj_2[obj_2>6]) ####
    print(4 in obj_2)     #####
    print("a" in obj_2)
    print(obj_2*3)
    print(np.exp(obj_2))

sdata={'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
obj_4 = pd.Series(sdata, index=["California", "Ohio", "Oregon", "Texas"])
obj_5 = pd.Series(sdata, index=["California", "Ohio", "Texas", "Oregon"])
obj_6 = pd.Series(sdata, index=["Utah", "Ohio", "California", "Texas"])
def check_3():
    obj_3 = pd.Series(sdata)
    print(obj_3)

    print(obj_4)
    print(pd.isnull(obj_4))
    print(pd.notnull(obj_4))
    print(obj_4.isnull())
    print(obj_4.notnull())
def check_4():

    print(obj_5+obj_6)
    obj_4 = pd.Series(sdata, index=["California", "Ohio", "Oregon", "Texas"])
    obj_4.name = "Population"
    obj_4.index.name = "State"
    print(obj_4)


