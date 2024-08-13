import os,json
os.system("cls")

dic = {
    'keys_0':'value_0',
    'keys_1':'value_1',
    'keys_2':'value_2',
    'keys_3':'value_3'
}
dic_2= {}

elements = list(dic.items())
for (key,value) in elements:
    dic_2[value]= key
print(json.dumps(dic_2, indent=2))