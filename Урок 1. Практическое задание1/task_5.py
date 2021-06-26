"""
Задание 5.
Задание на закрепление навыков работы со стеком

Реализуйте структуру "стопка тарелок".

Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.

Структура должна предусматривать наличие нескольких стеков.
Создание нового стека происходит при достижении предыдущим стеком порогового значения.
Реализуйте по аналогии с примером, рассмотренным на уроке, необходимые методы,
для реализации это структуры, добавьте новые методы (не рассмотренные в примере с урока)
для реализации этой задачи.

После реализации структуры, проверьте ее работу на различных сценариях

Подсказка:
Отдельне стопки можно реализовать через:
1) созд-е экземпляров стека (если стопка - класс)
или
2) lst = [[], [], [], [],....]

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.

Задание творческое. Здесь нет жестких требований к выполнению.
"""
import copy


# создаем класс "Стопка тарелок"
class StackOfPlates:
    # Хранилище стопок тарелок
    lst_stack = []

    def __init__(self):
        self.elems = []

    # метод для нахождения длины хранилища стопок тарелок
    @staticmethod
    def len_lst_stack():
        return len(StackOfPlates.lst_stack)

    # метод добавления копии списка(стопки тарелок-стека) в хранилище стеков

    def lst_stack_add(self):
        a = self.elems.copy()
        return StackOfPlates.lst_stack.append(a)

    # добавление элемента в "стопку тарелок"
    def add_plate(self, el):
        if self.stack_size() < 5:
            return self.elems.append(el)
        else:
            self.lst_stack_add()
            self.elems.clear()
            return self.add_plate(el)

    # метод удаления верхнего элемента стека
    def delete_plate(self):
        return self.elems.pop()

    # нахождение длины стека

    def stack_size(self):
        return len(self.elems)


if __name__ == '__main__':
    # Создание стека
    a = StackOfPlates()
    # добавление в стек 22 элемента
    a.add_plate('6')
    a.add_plate('7')
    a.add_plate('8')
    a.add_plate('9')
    a.add_plate('10')
    a.add_plate('11')
    a.add_plate('12')
    a.add_plate('13')
    a.add_plate('14')
    a.add_plate('15')
    a.add_plate('тарелка')
    a.add_plate('6')
    a.add_plate('7')
    a.add_plate('8')
    a.add_plate('9')
    a.add_plate('10')
    a.add_plate('11')
    a.add_plate('12')
    a.add_plate('13')
    a.add_plate('14')
    a.add_plate('15')
    a.add_plate('тарелка')
    # показать список со стеками
    print(list(StackOfPlates.lst_stack))
    # показать последний стек
    print(a.elems)
    # удалить верхний элемент из стека
    a.delete_plate()
    print(a.elems)
    # показать длину списка стеков
    print(StackOfPlates.len_lst_stack())