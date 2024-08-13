import os, json
os.system("cls")

string = "Bootcamp Foundation N2"
dic  = {}

for harf in string:
    dic[harf] = string.count(harf)
print(json.dumps (dic, indent = 2))