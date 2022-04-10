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

def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = random.choice(array)
    s_arr = []
    m_arr = []
    l_arr = []
    for item in array:
        if item < pivot:
            s_arr.append(item)
        elif item > pivot:
            l_arr.append(item)
        elif item == pivot:
            m_arr.append(item)
        else:
            raise Exception('Unknown situation')
    return quick_sort(s_arr)+m_arr+quick_sort(l_arr)

def quick_sort_no_memory(array,frst,lst):
    if frst >= lst:
        return
    pivot = array[random.randint(frst,lst)]
    i,j = frst,lst
    while i <= j:
        while array[i]<pivot:
            i+=1
        while array[j]>pivot:
            j-=1
        if i <= j:
            array[i],array[j] = array[j], array[i]
            i,j = i+1,j-1
    quick_sort_no_memory(array, frst, j)
    quick_sort_no_memory(array, i, lst)

array = [i for i in range(-10, 10)]
print(array)
random.shuffle(array)
print(array)
#bubble_sort(array)
#selection_sort(array)
#insertion_sort(array)
#shell_sot(array)
#arr_new = quick_sort(array)
#print(arr_new)
quick_sort_no_memory(array,0,len(array)-1)
print(array)