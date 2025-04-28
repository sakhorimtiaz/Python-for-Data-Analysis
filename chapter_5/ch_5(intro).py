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

obj_7=pd.Series([9,3,-2])
def check_5():
    # print((obj_7))
    obj_7.index = ["Maruf", "Miraj", "Jony"]
    print(obj_7)
    obj_4.index = ["a", "b", "c", "d"]
    print(obj_4)

data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002, 2003],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
frame=pd.DataFrame(data)
obj_8=pd.Series(data)

def check_6():
    print(data)
    print(obj_8)
    print(frame)    # entire data
    print(frame.head())  # 1st 5 rows
    print(pd.DataFrame(data, columns=["pop", "year", "state"]))

frame_2=pd.DataFrame(data,columns=["pop", "year", "state","debt"],index=["a","b","c","d","e","f"])
def check_7():
    print(frame_2)
    print(frame_2.index)
    print(frame_2.columns)
    print(frame_2["state"])   #best practice
    print(frame_2.state)     #not recomended
    print(frame_2.loc["c"])

def check_8():
    frame_2["debt"] = 16.5
    print(frame_2)
    frame_2["debt"] = np.arange(6)
    print(frame_2)
    val = pd.Series([1.6, 1.65, 1.62], index=["b", "c", "e"])
    frame_2["debt"] = val
    print(frame_2)
