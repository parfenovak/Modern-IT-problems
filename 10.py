#1

def read_matrix_from_file(filename):
    with open(filename, 'r') as file:
        matrix = [list(map(int, line.split())) for line in file]
    return matrix

def write_results_to_file(filename, sum_positive, count_positive):
    with open(filename, 'w') as file:
        file.write(f"Сумма положительных элементов над главной диагональю: {sum_positive}\n")
        file.write(f"Количество положительных элементов над главной диагональю: {count_positive}\n")

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

# Основной код
input_filename = 'ПарфеноваЕЕ_ЗИТ-24м_vvod.txt'
output_filename = 'ПарфеноваЕЕ_ЗИТ-24м_vivod.txt'

matrix = read_matrix_from_file(input_filename)
sum_positive, count_positive = sum_and_count_above_diagonal(matrix)
write_results_to_file(output_filename, sum_positive, count_positive)

#2
def read_matrix_from_file(filename):
    with open(filename, 'r') as file:
        matrix = [list(map(int, line.split())) for line in file]
    return matrix

def write_matrix_to_file(filename, matrix):
    with open(filename, 'w') as file:
        for row in matrix:
            file.write(" ".join(map(str, row)) + "\n")

def swap_min_max_in_rows(matrix):
    for row in matrix:
        min_val = min(row)
        max_val = max(row)
        min_index = row.index(min_val)
        max_index = row.index(max_val)
        row[0], row[min_index] = row[min_index], row[0]
        row[-1], row[max_index] = row[max_index], row[-1]
    return matrix

# Основной код
input_filename = 'ПарфеноваЕЕ_ЗИТ-24м_vvod.txt'
output_filename = 'ПарфеноваЕЕ_ЗИТ-24м_vivod.txt'

matrix = read_matrix_from_file(input_filename)
modified_matrix = swap_min_max_in_rows(matrix)
write_matrix_to_file(output_filename, modified_matrix)