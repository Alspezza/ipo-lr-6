#Вариант 1 Специан Захар
import random
stroki = random.randint(4,8)
stolbci = random.randint(4,8)

summa = 0
list1 =  [-3, -5, -2, -12, 0, 15, 4, 7, 2]
matrix = []
row = []
for x in range(stroki):
    row = []
    for i in range(stolbci):
        row.append(random.choice(list1))
    matrix.append(row)

for row in matrix:
    for num in row:
        print(f"{num:3d}", end=" ")
    print()
print("Количество строк, столбцов: ", stroki, " | ", stolbci)

for strok in matrix:
    for chislo in strok:
        if (chislo % 2 == 0):
            summa += chislo
print ("Сумма всех четных чисел в матрице: ", summa)
