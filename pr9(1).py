
def is_magic(matrix):
    summ = sum(matrix[0])
 
    for i in range(len(matrix)):
        temp = 0
        for j in range(len(matrix)):
            temp += matrix[j][i]
        if temp != summ or sum(matrix[i]) != summ:
            return False
    return True

with open("D:\\folder\\belyaevii_um222vvod.txt","r") as f:
    data = [[int(num) for num in line.split(',')] for line in f]
print(data)
mat = data
if (is_magic(mat)):
    file = open("D:\\folder\\belyaevii_um222vivod.txt","r")
    print(file.read())
    file.close()
    file = open("D:\\folder\\belyaevii_um222vivod.txt", 'w')
    print(file.write('Матрица является магическим квадратом'))
    file.close()
else:
    file = open("D:\\folder\\belyaevii_um222vivod.txt","r")
    print(file.read())
    file.close()
    file = open("D:\\folder\\belyaevii_um222vivod.txt", 'w')
    print(file.write('Матрица не является магическим квадратом'))
    file.close()