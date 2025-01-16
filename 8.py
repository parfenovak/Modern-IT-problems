#1 

def input_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            element = int(input(f"Введите [{i}, {j}] элемент: "))
            row.append(element)
        matrix.append(row)
    return matrix
def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))
def sum_and_count_above_diagonal(matrix):
    n = len(matrix)
    total_sum = 0
    count = 0

    for i in range(n):
        for j in range(i + 1, n):
            if matrix[i][j] > 0:
                total_sum += matrix[i][j]
                count += 1

    return total_sum, count
rows = int(input("Количество строк: "))
cols = int(input("Количество столбцов: "))
print("Введите элементы матрицы:")
matrix = input_matrix(rows, cols)
print("Исходный массив:")
print_matrix(matrix)
sum_positive, count_positive = sum_and_count_above_diagonal(matrix)
print(f"Сумма положительных элементов над главной диагональю: {sum_positive}")
print(f"Количество положительных элементов над главной диагональю: {count_positive}")

#2
def input_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            element = int(input(f"Введите [{i}, {j}] элемент: "))
            row.append(element)
        matrix.append(row)
    return matrix
def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))
def swap_min_max_in_rows(matrix):
    for row in matrix:
        min_val = min(row)
        max_val = max(row)
        min_index = row.index(min_val)
        max_index = row.index(max_val)
        row[0], row[min_index] = row[min_index], row[0]
        row[-1], row[max_index] = row[max_index], row[-1]
    return matrix
rows = int(input("Введите количество строк: "))
cols = int(input("Введите количество столбцов: "))
print("Введите элементы матрицы:")
matrix = input_matrix(rows, cols)
print("Исходный массив:")
print_matrix(matrix)
modified_matrix = swap_min_max_in_rows(matrix)
print("Полученный массив:")
print_matrix(modified_matrix)
