#1

import math
def area_circle(radius):
    return math.pi * radius ** 2
def area_rectangle(length, width):
    return length * width
def area_triangle(base, height):
    return 0.5 * base * height

radius = float(input("Радиус круга: "))
length = float(input("Длина прямоугольника: "))
width = float(input("Ширина прямоугольника: "))
base = float(input("Основание треугольника: "))
height = float(input("Высота треугольника: "))

print("Площадь круга с радиусом", radius, ":", area_circle(radius))
print("Площадь прямоугольника со сторонами",length,"и",width,":",area_rectangle(length, width))
print("Площадь треугольника с основанием",base,"и высотой",height,":",area_triangle(base, height))


#2
def sum_and_average(arr):
    total_sum = sum(arr)
    average = total_sum / len(arr)
    return total_sum, average

def input_array():
    while True:
        n = int(input("Количество элементов массива (не больше 15): "))
        if 1 <= n <= 15: 
            break
        else:
            print("Ошибка: размер массива не должен превышать 15.")

    arr = []
    for i in range(n):
        element = int(input(f"Введите элемент {i + 1}: "))
        arr.append(element)
    return arr

print("Ввод массива 1:")
array1 = input_array()

print("Ввод массива 2:")
array2 = input_array()

print("Ввод массива 3:")
array3 = input_array()

sum1, avg1 = sum_and_average(array1)
sum2, avg2 = sum_and_average(array2)
sum3, avg3 = sum_and_average(array3)

print("Массив 1: Сумма =", sum1, "Среднее =", avg1)
print("Массив 2: Сумма =", sum2, "Среднее =", avg2)
print("Массив 3: Сумма =", sum3, "Среднее =", avg3)