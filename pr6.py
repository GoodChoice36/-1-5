#Вариант 2 Задание 1
n=int(input("Ввести длинну массива"))
x=[]
for i in range(n):
    print("Введите элемент массива",i+1)
    x.append(int(input()))
    print(x)
    m=min(x)
    d=x.index(min(x))
print("Минимальный элемент массива:",m,"Индекс:",d)

#Вариант 2 Задание 2
n=int(input("Введите длинну массива:"))
x=[]
y=[]
z=[]
for i in range(n):
    print("Введите элемент массива",i+1)
    x.append(int(input()))
    print("Исходный массив:",x)
for i in range(n):
    if (x[i])>=0:
        y.append(x[i])
    if (x[i])<=0:
        z.append(x[i])
print("Положительные элементы:",y)
print("Отрицательные элементы:",z)