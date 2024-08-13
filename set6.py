import os, json
os.system("cls")

dic = {
    'name': 'Kelly',
    'age': 25,
    'salary': 8000,
    'city': 'New York'     
}
keys= dic.pop('city')
dic['location'] = keys
print(json.dumps(dic,indent=2))


