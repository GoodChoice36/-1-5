import math
a = int(input("Введите a:"))
b = int(input("Введите b:"))
c = int(input("Введите c:"))
if (a >=1) and  (a <=3):
    print(a)
if (b >=1) and (b<=3):
    print(" ",b)
if (c >=1)and (c<=3):
    print("  ",c)
elif((a <1) or (a >3))and ((b <1) or(b>3))and((c <1)or (c>3)):
    print("Ни одно число не находится в интервале [1,3]")