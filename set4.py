import os, json
os.system("cls")

keys = ['Ten:', "Twenty:", 'Thirty:']
values = [10, 20, 30]
dic = {
    'name': 'Bekzod'
}
for i in range (len(keys)):
    dic[keys[i]] = values[i]
print(dic)