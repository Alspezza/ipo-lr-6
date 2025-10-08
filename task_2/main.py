#Вариант 1 Специан Захар
import random
stroki = random.randint(4,8)
stolbci = random.randint(4,8)

list1 =  [-3, -5, -2, -12, 0, 15, 4, 7, 2]
matrix = []
for strok in range(stroki):
    for stolb in range(stolbci):
        matrix.append(random.choice(list1))
for stroki in matrix:
    for num in stroki:
        print(f"{num:3d}", end=" ")
