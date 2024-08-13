import os,json
os.system("cls")

dic1= {
    'key1': 1,
    'key2': 2,
    'key3': 3  
}
dic2= {
    'key1':1,
    'key2':2 
}
st1 = set(dic1.items())
st2 = set(dic2.items())
result = st1.intersection(st2)
dic_same = set(result)

print(dic_same)