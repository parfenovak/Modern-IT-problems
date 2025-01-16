#1
n = int(input('Введите длину массива: '))
a = [
     for i in range(n)]
max_element = max(a)
reversed_array = a[::-1]
print('Максимальный элемент:', max_element)
print('Массив в обратном порядке:', reversed_array)

#2
input_string = input('Введите элементы массива через пробел: ')
a = list(map(float, input_string.split()))
average = sum(a) / len(a)
for i in range(len(a)):
    if a[i] == 0:
        a[i] = average
print('Среднее арифметическое элементов массива:', average)
print('Массив после замены нулевых элементов:', a)