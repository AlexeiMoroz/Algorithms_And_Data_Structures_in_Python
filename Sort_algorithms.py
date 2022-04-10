#Bubble sort

import random

def bubble_sort(array):
    n = 1
    while n < len(array):
        for i in range(len(array)-n):
            if array[i]>array[i+1]:
                array[i], array[i+1] =  array[i+1],array[i]
        n+=1



array = [i for i in range(-100, 100)]
print(array)
random.shuffle(array)
print(array)
bubble_sort(array)
print(array)
