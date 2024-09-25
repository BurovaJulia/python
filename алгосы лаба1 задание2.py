# Задание 2

import numpy as np

matrix_A = np.random.randint(0, (10**5)*3, ((10**4)*3, (10**4)*3))  # создали случ матрицу n*n
matrix_B = np.random.randint(0, (10**5)*3, ((10**4)*3, (10**4)*3))
#matrix_A = np.random.randint(0, 5, (3, 3))  # границы допустимых значений, размер матрицы
#matrix_B = np.random.randint(0, 5, (3, 3))

def multiplication_of_mats(m1, m2):
    matrix_C = np.full((len(m1), len(m2)), 0)
    for i in range(len(m1)):
        for j in range(len(m2)):
            for k in range(len(m1)):
                matrix_C[i][j] += m1[i][k] * m2[k][j]
    return (matrix_C)

#print(matrix_A, matrix_B, sep='\n\n', end='\n\n')

for n in range (1, (10**5)*17, 1700):
#for n in range (1, 4):
    m_A = matrix_A[:n, :n]  # от большой матрицы берем маленькие матрицы
    m_B = matrix_B[:n, :n]
    print(multiplication_of_mats(m_A, m_B), sep='\n\n', end='\n\n')
