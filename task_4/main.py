#запрашиваем строку для поиска
sstring = input("Введите строку для поиска: ").strip().lower()
#читаем файл
with open(r'C:\Users\user\Desktop\Лабы и тп\ИПО\lr6\task_4\text.txt', 'r', encoding='utf-8') as file:
    lines = [line.strip() for line in file]
#ищем строки с подстрокой
found_lines = [line for line in lines if sstring in line.lower()]
#выводим результаты
print("Найдено строк: ", len(found_lines))
for line in found_lines:
    print(line)
#сортируем и выводим по длине
print("Отсортировано по длине:")
for line in sorted(found_lines, key=len):
    print(line)
