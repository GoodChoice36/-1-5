import numpy as np
N = 2
M = 3

with open("D:\\folder\\belyaevii_um222input.txt","r") as f:
    A = [[int(num) for num in line.split(',')] for line in f]
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
        with open("D:\\folder\\belyaevii_um222output.txt", "a") as result:
                np.savetxt("D:\\folder\\belyaevii_um222output.txt", A[i][j])
    print()