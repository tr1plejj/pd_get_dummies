import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10

random.shuffle(lst)

header = {}

for item in lst:
    if header.get(item) == None:
        header[item] = []

for element in lst:
    for key in header.keys():
        value = header.get(key)
        if key != element:
            value.append(0)
        else:
            value.append(1)

data = pd.DataFrame(header)
data.head(n = 20)
          
print(data)