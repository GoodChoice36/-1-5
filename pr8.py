#Задание1 Вариант2
def is_magic(matrix):
    summ = sum(matrix[0])
 
    for i in range(len(matrix)):
        temp = 0
        for j in range(len(matrix)):
            temp += matrix[j][i]
        if temp != summ or sum(matrix[i]) != summ:
            return False
    return True
            
mat = [[4, 3, 3], [3, 4, 3], [3, 3, 4]]
print("Исходная матрица:",mat)
if (is_magic(mat)):
    print( "Матрица является магическим квадратом")
else :
    print( "Матрица не является магическим квадратом")
#Задание2 Вариант2
N = 3
M = 4

A = [
[1, 2, 3, 4],
[5, 6, 7, 8],
[9,10,11,12]]
print("Исходная матрица:")
for i in range(N):
    print(A[i])
print("Полученная матрица:")
for i in range(N):
    tmp = A[i][0]
    A[i][0] = A[i][M-1]
    A[i][M-1] = tmp
for i in range(N):
    for j in range(M):
        print("%4d " % A[i][j], end='')
    print()