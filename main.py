def check_duplicate(list2:list):
    marks = set()
    with open('output.txt', 'a',encoding='UTF-8') as file:
        for mark in list2:
            if mark in marks:
                file.write(f"Есть повтор:\n{mark}\n")
            else:
                marks.add(mark)

def check_difference(list1:list,list2:list):
    with open('output.txt','a',encoding='UTF-8') as file:
        diff = list(set(list2) ^ set(list1))
        if diff != []:
            file.write("Разница между двумя списками:\n")
            for d in diff:
                file.write(str(d)+'\n')
        if diff == []:
            file.write("Нет разницы\n")

# Определяем минимальную и максимальную длину штрихкодов
min_length = 150
max_length = 150


# Считываем штрихкоды из первого файла
with open('file1.txt', 'r') as f1:
    list1 = [line.strip().replace('<gz:NCode>','').replace('</gz:NCode>','') for line in f1 if len(line.strip().replace('<gz:NCode>','').replace('</gz:NCode>','')) >= min_length and len(line.strip().replace('<gz:NCode>','').replace('</gz:NCode>','')) <= max_length]

# Считываем штрихкоды из второго файла
with open('file2.txt', 'r') as f2:
    list2 = [line.strip() for line in f2 if len(line.strip()) >= min_length and len(line.strip()) <= max_length]

with open('output.txt', 'w',encoding='UTF-8') as file:
    file.write('')

check_duplicate(list2)
check_difference(list1,list2)
# Находим разницу между массивами
