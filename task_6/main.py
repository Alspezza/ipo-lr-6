#импортируем библиотеку рандом и создаем нужные переменные
import random
list = []
y = 0
#система циклов для создание листа, состоящего из 20 значений по 4 числа от -10 до 10
for i in range(20):
    minilist = []
    for x in range(4):
        minilist.append(random.randint(-10,10))
    list.append(minilist)
#создаем кортеж unique и записываем в него все отсортрованные оригинальные значения
unique = {tuple(sorted(znach)) for znach in list}
chislo = int(input("Введите число: "))
#находим сумму каждого из 20 элементов и сравниваем с введенным пользователем числом
for i in unique:
    sum = i[0] + i[1] + i[2] + i[3] 
    print(f"{i} | Сумма: {sum}")
    if chislo > sum:
        y += 1
print("Количество комбинаций меньше чем",chislo,": ",y) #выводим все
