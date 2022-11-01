#Задание 1-2
a = int(input("Введите A"))
b = int(input("Введите B"))
if (a<b):
    for i in range(a,b+1):
        print(i, end="; ")
elif (a>b):
    for i in range(a,b-1,-1):
         print(i, end= "; ")
         
         
#Задание 3
a = int(input("Введите A"))
b = int(input("Введите B"))
if (a>b):
    for i in range(a,b-1,-1):
        print(i, end= "; ")
else:
    print("А должно быть больше чем В")