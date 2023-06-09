# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     3
#     -> 1

from random import randint

count_element = int(input("Введите количество элементов: "))
list_numbers = []
for i in range(count_element):
    list_numbers.append(randint(0,5))
print("Содержимое листа:")
print(list_numbers)
find_num = int(input("Введите число: "))
count_repeat_num = 0
for i in range(len(list_numbers)):
    if find_num == list_numbers[i]:
        count_repeat_num += 1
print(f"Число {find_num} встречается {count_repeat_num} раз")