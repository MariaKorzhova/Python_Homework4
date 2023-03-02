# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах. 
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств. 

# 11 6 
# 2 4 6 8 10 12 10 8 6 4 2 
# 3 6 9 12 15 18 
# 6 12 

def intersection_list(list1, list2): 
   return set(list1).intersection(list2) 

n = int(input("Введите количество элементов первого списка: "))
m = int(input("Введите количество элементов второго списка: "))
lst1 = []
lst2 = []
for i in range(n):
    lst1.append(int(input("Введите элемент первого списка: ")))
for i in range(m):
    lst2.append(int(input("Введите элемент второго списка: ")))
print(lst1)
print(lst2)
new_lst = list(intersection_list(lst1, lst2))
new_lst.sort()
print(new_lst)



# if n >= m:
#     for i in range(len(lst1)):
#         if lst1[i] in lst2:
#             new_lst.append(lst1[i])
# else:
#     for j in range(len(lst2)):
#         if lst2[j] in lst1:
#             new_lst.append(lst2[j])
# new_lst.sort()
# print(new_lst)



