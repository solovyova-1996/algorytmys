"""
Задание 1.

Для каждой из трех функций выполнить следующее:

1) для каждого выражения вместо !!! укажите сложность этого выражения.
2) определите сложность каждой функции в целом.

Сложность нужно определять только там, где указаны символы !!!

Примечание:
Прошу вас внимательно читать ТЗ и не выполнять все пункты.
"""

import random


#############################################################################################
def check_1(lst_obj):
    """Функция должна создать множество из списка.

    Алгоритм 3:
    Создать множество из списка

    Сложность: O(n) - линейная
    """
    lst_to_set = set(lst_obj)  # O(n) - линейная (зависит от len(lst_obj))
    return lst_to_set  # O(1) - константная сложность


#############################################################################################
def check_2(lst_obj):
    """Функция должная вернуть True, если все элементы списка различаются.

    Алгоритм 1:
    Проходимся по списку и для каждого элемента проверяем,
    что такой элемент отстутствует
    в оставшихся справа элементах

    Сложность: O(n) - линейная сложность
    """
    for j in range(len(lst_obj)):          # O(n) + O(1) + O(1) = O(n) - Линейная сложность
        if lst_obj[j] in lst_obj[j+1:]:    # O(n) - линейная сложность
            return False                   # O(1) - константная сложность
    return True                            # O(1) - константная сложность


#############################################################################################
def check_3(lst_obj):
    """Функция должная вернуть True, если все элементы списка различаются.

    Алгоритм 2:
    Вначале выполним для списка сортировку, далее, сравниваем элементы попарно
    Если присутствуют дубли, они будут находиться рядом.

    Сложность: O(n log n) - линейно-логарифмическая
    """
    lst_copy = list(lst_obj)                 # O(n) - линейная сложность
    lst_copy.sort()                          # O(n log n) - линейно-логарифмическая
    for i in range(len(lst_obj) - 1):        # O(n) - линейная сложность
        if lst_copy[i] == lst_copy[i+1]:     # O(1) -  константная сложность
            return False                     # O(1) - константная сложность
    return True                              # O(1) - константная сложность

#############################################################################################


for j in (50, 500, 1000, 5000, 10000):
    # Из 100000 чисел возьмем 'j' случайно выбранных
    # Всего 10 тыс. чисел
    lst = random.sample(range(-100000, 100000), j)

print(check_1(lst))
print(check_2(lst))
print(check_3(lst))
