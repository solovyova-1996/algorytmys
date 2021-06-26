"""
Задание 4.

Для этой задачи:
1) придумайте 2-3 решения (не менее двух)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Сама задача:
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.

Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.

Приложение должно давать ответы на эти вопросы и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.

Задание творческое. Здесь нет жестких требований к выполнению.
"""

import json

# # Решение №1- это вариант решения в котором реализуется механизм активации учетной записи,
# то есть при активации метка активации меняется в хранилище(не поняла по заданию нужно это или нет)
storage = {'login1': [1234, True], 'login2': [3434, False], 'login3': [5656, True]}
with open(r'D:\обучение\Алгоритмы и структуры данных на Python\file1.json', 'w', encoding='utf-8') as f:
    json.dump(storage, f)


def authentication(login,password):
    with open(r'D:\обучение\Алгоритмы и структуры данных на Python\file1.json', 'r', encoding='utf-8') as f:
        storage = json.load(f)
    if login not in storage.keys():
        return f'неверный логин'
    if login in list(storage.keys()) and password == storage[login][0] and storage[login][1] == True:
        print("Вход в систему разрешен")
    elif login in list(storage.keys()) and password == storage[login][0] and storage[login][1] == False:
        activation = input("Ваша учетная запись неактивирована,для активации введите - 'да',"
                           "введите - 'нет'-для отмены активации:  ")
        if activation == 'Да' or activation == 'да' or activation == 'ДA':
            with open(r'D:\обучение\Алгоритмы и структуры данных на Python\file1.json', 'r', encoding='utf-8') as f:
                storage = json.load(f)
            storage[login][1] = True
            with open(r'D:\обучение\Алгоритмы и структуры данных на Python\file1.json', 'w', encoding='utf-8') as f:
                json.dump(storage, f)
            print('Учетная запись активирована,вход в систему разрешен')
            login = input("Введите логин:  ")
            password = int(input("Введите пароль:  "))
            b = authentication(login,password)
    elif login in list(storage.keys()) and password != storage[login][0] and storage[login][1] == True:
        print('Неверный пароль.Попробуйте снова.')
        password = int(input("Введите пароль:  "))
        a = authentication(login,password)



login = input("Введите логин:  ")
password = int(input("Введите пароль:  "))

res = authentication(login,password)
# Решение №1 у данного решения линеная сложность O(n)
# Это тот же вариант, но с условной активацией
def authentication1(login, password, storage):
    if login not in storage.keys():
        return f'неверный логин'
    passw = storage[login][0]                                                             # O(1) - константная
    activation_label = storage[login][1]                                                  # O(1) - константная
    if login in storage.keys() and password == passw and activation_label:               # O(n) - линейная
        return f'Вход в систему разрешен'                                                 # O(1) - константная
    elif login in storage.keys() and password == passw and activation_label == False:     # O(n) - линейная
        activation = input("Ваша учетная запись неактивирована,для активации введите - 'да',"
                           "введите - 'нет'-для отмены активации:  ")                     # O(1) - константная
        if activation in ('Да','да','ДА'):                                                # O(1) - константная
            return f'Учетная запись активирована,вход в систему разрешен'                 # O(1) - константная
    elif login in storage.keys() and password != passw and activation_label:              # O(n) - линейная
        password = int(input("Неверный пароль.Попробуйте снова. Введите пароль: "))       # O(1) - константная
        if password == passw:                                                             # O(1) - константная
            return f'Вход в систему разрешен'                                             # O(1) - константная
        else:
            return f'Неверный пароль'                                                     # O(1) - константная


storage = {'login1': [1234, True], 'login2': [3434, False], 'login3': [5656, True]}       # O(1) - константная
login = input("Введите логин:  ")                                                         # O(1) - константная
password = int(input("Введите пароль:  "))                                                # O(1) - константная
res = authentication1(login, password, storage)                                           # O(n) - линейная
print(res)                                                                                # O(1) - константная

# Решение №2 сложность решения квадратичная  O(n^2)
def authentication2(login, password, storage):
    if login not in storage.keys():
        return f'неверный логин'
    for key in storage.keys():
        if key == login:
            for val in storage.values():
                if password == storage[login][0] and password == val[0] and storage[login][1] == True:
                    return f'Вход в систему разрешен'
                elif password != storage[login][0] and storage[login][1] == True:
                    return f'Неверный пароль'
                elif password == storage[login][0] and password == val[0] and storage[login][1] == False:
                    activation = input("Ваша учетная запись неактивирована,для активации введите - 'да':  ")
                    if activation == 'Да' or activation == 'да' or activation == 'ДA':
                        return f'Учетная запись активирована,вход в систему разрешен'
                    else:
                        return f'Учетная запись не активирована'


storage = {'login1': [1234, True], 'login2': [3434, False], 'login3': [5656, True]}
login = input("Введите логин:  ")
password = int(input("Введите пароль:  "))
res = authentication2(login, password, storage)
print(res)

# Вывод: эффективнее решение №1 так, как имеет линейную сложность и при увеличении объема данных
# будет выполняться быстрее, чем решение №2








