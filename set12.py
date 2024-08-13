import os, json
os.system("cls")

dic1 = {}
dic2 = {}

n = int(input("Nechta kalit va qiymat kiritmoqchisiz: "))
for i in range(n):
    key = input("Kalit kiriting: ")
    value = input("Qiymat kiriting: ")
    dic1[key] = value
print("Birinchi dictionary :")
print(json.dumps(dic1, indent=2))

n = int(input("Nechta kalit va qiymat kiritmoqchisiz (dic2): "))
for i in range(n):
    key = input("Kalit kiriting: ")
    value = input("Qiymat kiriting: ")
    dic2[key] = value
print("Ikkinchi dictionary :")
print(json.dumps(dic2, indent=2))

def dictionaries(dict1, dict2):
    new_dict = dict1.copy()  
    new_dict.update(dict2)  
    return new_dict

new_dct = dictionaries(dic1, dic2)

print("Qo'shilgan dictionary:")
print(json.dumps(new_dct, indent=2))
