#Задание1
import math
a = int(input("Введите сторону a:"))
s = (3*(3**0.5)*a**2)/2
print("s = {0:.2f}".format(s))

#Задание2
a1 = int(input("Введите длинну первого прямоугольника:"))
b1 = int(input("Введите ширину первого прямоугольника:"))
s1 = a1*b1
a2 = int(input("Введите длинну второго прямоугольника:"))
b2 = int(input("Введите ширину второго прямоугольника:"))
s2 = a2*b2
a3 = int(input("Введите длинну третьего прямоугольника:"))
b3 = int(input("Введите ширину третьего прямоугольника:"))
s3 = a3*b3
print("Площадь первого прямоугольника",s1)
print("Площадь второго прямоугольника",s2)
print("Площадь третьего прямоугольника",s3)