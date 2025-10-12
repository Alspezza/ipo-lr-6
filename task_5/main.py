import random
list1 = []
kolvo_more = 0
kolvo_less = 0
for i in range(25):
    list1.append(random.randint(-50,50))
for i in list1: 
    if i>0: 
        kolvo_more +=1
for i in list1: 
    if i<0: 
        kolvo_less +=1

print(list1)
more = [chislo for chislo in list1 if chislo > 0 ]
less = [chislo for chislo in list1 if chislo < 0]
zero = [chislo for chislo in list1 if chislo == 0]
proc_m = float(kolvo_more / 25 * 100)
proc_l = float(kolvo_less / 25 * 100)
print("Положительные числа(",proc_m,"% ): ",more, " их количество - ", kolvo_more)
print("Отрицательные числа(",proc_l,"% ):",less, " их количество - ", kolvo_less)
if zero == []: print("Нули отсутствуют") 
else : print("Нули присутствуют(",100 - proc_l - proc_m,"% ), их количество: ", 25 - kolvo_more - kolvo_less)
