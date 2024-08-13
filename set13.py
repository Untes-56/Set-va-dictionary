import os,json
os.system("cls")

num = int(input("Son kiriting:"))
dictionary = {}
a=1, b=1
for i in range(1, num+1):
    dictionary[i] = a
    c = a + b
    a = b
    b = c
print(json.dumps(dictionary, indent=2))     
     