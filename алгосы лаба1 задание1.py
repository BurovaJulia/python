#Задание №1

import time
import numpy as np
import matplotlib.pyplot as plt

vec = np.random.randint(1, (10**4)*3, (10**4)*3)  # создали огромный вектор со случ значениями
#vec = np.random.randint(1, 11, 10)  # нижний диапазон вкл, верх диапазон не вкл, длина
#print(vec, end='\n\n')

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

def average_t(times):
    return sum(times) / len(times)

def build_graph(time, range_):
    plt.plot(range_, time)
    plt.xlabel('Размер массива, n')
    plt.ylabel('Среднее время выполнения, sec')
    plt.title('Зависимость времени от размера массива')
    plt.show()
    plt.grid(True)

def time_measurement():
    execution_time_sum = []  # список времени выполнения
    execution_time_max = []
    execution_time_min = []
    execution_time_harmonic = []
    n_values = []  # список значений при которых выполняются измерения

    for n in range(1, (10 ** 4) * 3, 300):
        v = vec[:n]
        single_times_sum = []  # список 5 замеров для каждого n
        single_times_max = []
        single_times_min = []
        single_times_harmonic = []
        for _ in range(5):
            start_time = time.time()
            sum_of_nums(v)
            end_time = time.time()
            single_times_sum.append(end_time - start_time)

            start_time = time.time()
            search_of_max(v)
            end_time = time.time()
            single_times_max.append(end_time - start_time)

            start_time = time.time()
            search_of_min(v)
            end_time = time.time()
            single_times_min.append(end_time - start_time)

            start_time = time.time()
            mid_harmonic(v)
            end_time = time.time()
            single_times_harmonic.append(end_time - start_time)

        avg_time_sum = average_t(single_times_sum)
        execution_time_sum.append(avg_time_sum)

        avg_time_max = average_t(single_times_max)
        execution_time_max.append(avg_time_max)

        avg_time_min = average_t(single_times_min)
        execution_time_min.append(avg_time_min)

        avg_time_harmonic = average_t(single_times_harmonic)
        execution_time_harmonic.append(avg_time_harmonic)

        n_values.append(n)

    build_graph(execution_time_sum, n_values)
    build_graph(execution_time_max, n_values)
    build_graph(execution_time_min, n_values)
    build_graph(execution_time_harmonic, n_values)
    # return execution_time_sum, execution_time_max, execution_time_min, execution_time_harmonic, n_values

time_measurement()
