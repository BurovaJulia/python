import time
import numpy as np
import matplotlib.pyplot as plt

n1 = 1000
n2 = 5000
n3 = 10000
n4 = 100000

list_n_sorted = list(range(0, n4 + 1))  # создали сортированный список
list_n_random = np.random.randint(0, n4, n4)  # создали рандомный список
list_n_resorted = list(range(n4 + 1, 0, -1))  # создали сортированный наоборот список

# Метод Шелла
def shell(list_):
    interval = len(list_) // 2
    while interval > 0:
        for i in range(interval, len(list_)):
            temp = list_[i]
            j = i
            while j >= interval and list_[j - interval] > temp:
                list_[j] = list_[j - interval]
                j -= interval

            list_[j] = temp
        interval //= 2

# Блинная сортировка
'''Алгоритм блинной сортировки:

Найти максимальный элемент.
Перевернуть цепочку элементов от левого края до максимума — в результате максимум окажется на левом крае.
Затем перевернуть весь неотсортированный подмассив, в результате чего максимум попадает на своё место.
Повторить эти действия с оставшейся неотсортированной частью массива. '''

def flip(list_, i):  # функция переворота массива
    start = 0
    while start < i:
        list_[start], list_[i] = list_[i], list_[start]
        start += 1
        i -= 1

def max_in_list_index(list_, size_):
    max_index = 0
    for i in range(size_):
        if list_[i] > list_[max_index]:
            max_index = i
    return max_index

def pancake(list_):
    cur_size = len(list_)
    while cur_size > 1:
        max_el_index = max_in_list_index(list_, cur_size)
        if max_el_index != cur_size - 1:
            flip(list_, max_el_index)
            flip(list_, cur_size - 1)
        cur_size -= 1

def build_graph(time, range_):
    plt.plot(range_, time)
    plt.xlabel('Размер массива, n')
    plt.ylabel('Среднее время выполнения, sec')
    plt.title('Зависимость времени от размера массива')
    plt.show()
    plt.grid(True)

def time_measurement(func):
    exe_time_sorted = []  # список времени выполнения
    exe_time_random = []
    exe_time_resorted = []
    n_values = [n1, n2, n3, n4]  # список значений при которых выполняются измерения

    for i in n_values:
        test_list_sorted = list_n_sorted[:i]
        test_list_random = list_n_random[:i]
        test_list_resorted = list_n_resorted[:i]

        start_time = time.time()
        func(test_list_sorted)
        end_time = time.time()
        exe_time_sorted.append(end_time - start_time)

        start_time = time.time()
        func(test_list_random)
        end_time = time.time()
        exe_time_random.append(end_time - start_time)

        start_time = time.time()
        func(test_list_resorted)
        end_time = time.time()
        exe_time_resorted.append(end_time - start_time)

    build_graph(exe_time_sorted, n_values)
    build_graph(exe_time_random, n_values)
    build_graph(exe_time_resorted, n_values)


time_measurement(shell)
time_measurement(pancake)
