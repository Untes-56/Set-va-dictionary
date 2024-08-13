import os,json
os.system("cls")

num = int(input("Son kiriting:"))
dic = {}
for i in range(num):
    key= 'key' +str(i)
    value = 'value' + str(i)
    dic[key] =  value
print(json.dumps(dic, indent=2))