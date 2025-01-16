#1

def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)

def fac(n):
    if n == 0:
        return 1
    else:
        return n * fac(n - 1)

def expression(x, n):
    return power(x, n) / fac(n)

x = int(input("Введите значение x: "))
n = int(input("Введите значение n: "))

result = expression(x, n)
print(f"Результат выражения {x}^{n} / {n}! = {result}")

#2
def find_max():
    num = int(input("Введите число: ")) 
    if num == 0:
        return 0
    else:
        max_rest = find_max() 
        return num if num > max_rest else max_rest  

print("Введите последовательность натуральных чисел (завершите ввод числом 0):")
max_value = find_max()
print("Наибольшее значение в последовательности:", max_value)