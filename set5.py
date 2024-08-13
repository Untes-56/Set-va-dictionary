import os
os.system("cls")

dic = {
    'a':100,
    'b':200,
    'c':300   
}

elements = list(dic.values())
print(elements)
count = False
for i in elements:
    if  i == 200:
        count = True
        
if count:
    print("Mavjud") 
else:
    print("Mavjud emas")
      
    