s = input('Ввод строки: ')
words = s.split()
count = 0
for word in words:
    if word.startswith('е') or word.startswith('Е'):
        count += 1
print(f'Количество слов, начинающихся с буквы "е": {count}')