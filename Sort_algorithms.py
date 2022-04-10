#Bubble sort

import random

def bubble_sort(array):

    n = 1
    while n < len(array):
        for i in range(len(array)-n):
            if array[i]<array[i+1]:
                array[i], array[i+1] =  array[i+1],array[i]
        n+=1

def selection_sort(array):

    for i in range(len(array)):
        idx_min = i
        for j in range(i+1, len(array)):
            if (array[idx_min]>array[j]):
                idx_min = j
        array[i],array[idx_min] = array[idx_min],array[i]

def insertion_sort(array):

    for i in range(1, len(array)):
        spam = array[i]
        j = i
        while array[j-1] > spam and j>0:
            array[j] = array[j - 1]
            j-=1
        array[j] = spam

def shell_sot(array):

    assert len(array)<4000,  'Only array before 200 numbers are allowed'
    def new_increment_array(array):
        inc = [1,4,10,23,57,132,301,701,1750]
        #print(inc[-1])

        while len(array)<inc[-1]:
            #print(inc[-1])
            inc.pop()

        while len(inc)>0:
            yield inc.pop()

    for increment in new_increment_array(array):
        for i in range(increment, len(array)):
            for j in range(i, increment - 1, -increment):
                if array[j-increment] <= array[i]:
                    break
                array[j], array[j-increment] = array[j-increment], array[j]




array = [i for i in range(-100, 100)]
print(array)
random.shuffle(array)
print(array)
#bubble_sort(array)
#selection_sort(array)
#insertion_sort(array)
shell_sot(array)
print(array)
