# Напишите функцию для транспонирования матрицы

Matrix = [[1, 2], [3, 4], [5, 6, 7]]

transonated_matrix = [[0 for i in range(len(Matrix))] for j in range(len(Matrix[0]))]
for j in range(len(Matrix)):
    for i in range(len(Matrix[0])):
        transonated_matrix[i][j] = Matrix[j][i]
print(Matrix)
print(transonated_matrix)