# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

import random

def merge_two_arrs(a, b):

   c = []
   i = j = 0
   while i < len(a) and j < len(b):
      if a[i]<b[j]:
         c.append(a[i])
         i += 1
      else:
         c.append(b[j])
         j += 1
   if i < len(a):
      c += a[i:]
   if j < len(b):
      c += b[j:]

   return c

def merge_sort(arr):

   if len(arr) == 1:
       return arr

   middle = len(arr)//2
   left = merge_sort(arr[:middle])
   right = merge_sort(arr[middle:])
   return merge_two_arrs(left, right)


lst = [random.uniform(0, 50) for _ in range(10)]
print(f'Список до сортировки:\n{lst}')
new_list = merge_sort(lst)
print(f'Список после сортировки:\n{new_list}')
