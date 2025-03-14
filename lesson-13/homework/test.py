import numpy as np
#task 1
print("Task 1")
vector = np.arange(10, 50)
print(vector)
#task 2
print("Task 2")
matrix = np.arange(9).reshape(3, 3)
print(matrix)
#task 3
print("Task 3")
identity_matrix = np.eye(3)
print(identity_matrix)
#task 4
print("Task 4")
array_3by3 = np.random.rand(3, 3,3)
print(array_3by3)
#task 5
print("Task 5")
array_10by10 = np.random.rand(10, 10)
print(array_10by10)
print(array_10by10.min())
print(array_10by10.max())
#task 6
print("Task 6")
vector_30 = np.random.rand(30)
print(np.mean(vector_30))
#task 7
print("Task 7")
random_5by5 = np.random.rand(5, 5)
normalized = (random_5by5 - random_5by5.min()) / (random_5by5.max() - random_5by5.min())
print(normalized)
#task 8
print("Task 8")
matrix_5by3 = np.random.rand(5, 3)
matrix_3by2 = np.random.rand(3, 2)
real_matrix_product = matrix_5by3 @ matrix_3by2
print(real_matrix_product)
#task 9
print("Task 9")
matrix_3by3_a = np.random.rand(3,3)
matrix_3by3_b = np.random.rand(3,3)
dot_product = np.dot(matrix_3by3_a, matrix_3by3_b)
print(dot_product)
#task 10 
print("Task 10")   
matrix_4by4 = np.random.rand(4,4)
transpose = matrix_4by4.T
print(transpose)
#task 11
print("Task 11")
matrix3by3 = np.random.rand(3,3)
determinant = np.linalg.det(matrix3by3)
print(determinant)
#task 12
print("Task 12")
A = np.random.rand(3,4)
B = np.random.rand(4,3)
matrix_product = np.matmul(A,B)
print(matrix_product)
#task 13
print("Task 13")
matrix_3x3 = np.random.rand(3, 3)
vector_3x1 = np.random.rand(3, 1)
matrix_vector_product = np.dot(matrix_3x3, vector_3x1)
print(matrix_vector_product)

#task 14
print("Task 14")
A = np.random.rand(3, 3)
b = np.random.rand(3, 1)
x = np.linalg.solve(A, b)
print(x)

#task 15
print("Task 15")
matrix_5x5 = np.random.rand(5, 5)
row_sums = matrix_5x5.sum(axis=1)
col_sums = matrix_5x5.sum(axis=0)
print(row_sums)
print(col_sums)