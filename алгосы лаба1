#Задание №1

import numpy as np
import random

vec = np.random.randint(0, (10**5)*3, (10**5)*3)  # создали огромный вектор со случ значениями
#vec = np.random.randint(1, 11, 10)  # нижний диапазон вкл, верх диапазон не вкл, длина
print(vec, end='\n\n')

def sum_of_nums(vector):
    sum_v = 0
    # return sum(vector)
    for i in vector:
        sum_v += i
    return sum_v

def search_of_max(vector):
    # return max(vector)
    max_v = vector[0]
    for i in range(1, len(vector)):
        if max_v < vector[i]:
            max_v = vector[i]
    return max_v

def search_of_min(vector):
    # return min(vector)
    min_v = vector[0]
    for i in range(1, len(vector)):
        if min_v > vector[i]:
            min_v = vector[i]
    return min_v

def mid_harmonic(vector):
    sum_vk = 0
    for i in range(len(vector)):
        sum_vk += 1/vector[i]
    return sum_vk

for n in range(1, (10**5)*3, 300):
#for n in range(1, 11, 2):
    v = vec[0:n]  # создаем мини-векторы для каждого случая
    print(sum_of_nums(v), search_of_max(v), search_of_min(v), n/mid_harmonic(v))
