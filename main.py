# Определяем минимальную и максимальную длину штрихкодов
min_length = 150
max_length = 150

# Считываем штрихкоды из первого файла
with open('file1.txt', 'r') as f1:
    list1 = [line.strip() for line in f1 if len(line.strip()) >= min_length and len(line.strip()) <= max_length]

# Считываем штрихкоды из второго файла
with open('file2.txt', 'r') as f2:
    list2 = [line.strip() for line in f2 if len(line.strip()) >= min_length and len(line.strip()) <= max_length]

# Находим разницу между массивами
diff = list(set(list1) - set(list2))
if diff != []:
    print("Разница между двумя списками:")
    print(diff)
if diff == []:
    print("Нет разницы")