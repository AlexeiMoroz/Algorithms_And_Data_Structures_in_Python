# 1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными
# числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.

import random

# def bubble_sort(array):
#
#     n = 1
#     while n < len(array):
#         for i in range(len(array) - n):
#             if array[i] < array[i+1]:
#                 array[i], array[i+1] =  array[i+1], array[i]
#         n += 1

def bubble_sort_modified(arr):
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

array = [i for i in range(-100, 100)]
random.shuffle(array)
print(array)
bubble_sort_modified(array)
print(array)

