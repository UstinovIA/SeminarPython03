# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

from random import randint

count_element = int(input("Введите количество элементов: "))
list_numbers = []
for i in range(count_element):
    list_numbers.append(randint(0,100   ))
print("Содержимое листа:")
print(list_numbers)
find_num = int(input("Введите число: "))
close_num = list_numbers[0]
min_distance = abs(find_num - close_num)
for i in range(1, len(list_numbers)-1):
    if min_distance > abs(find_num - list_numbers[i]):
        min_distance = abs(find_num - list_numbers[i])
        close_num = list_numbers[i]
print(f"Ближайшим числом к числу {find_num} является {close_num}")