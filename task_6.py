"""
Задание 6.
Задание на закрепление навыков работы с очередью

Реализуйте структуру "доска задач".

Структура должна предусматривать наличие несольких очередей задач, например,
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения

После реализации структуры, проверьте ее работу на различных сценариях

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.

Задание творческое. Здесь нет жестких требований к выполнению.
"""


class TasksQueue:
    # список решенных задач
    lst_solve_task = []

    @staticmethod
    def print_lst_solve_task():
        print(TasksQueue.lst_solve_task)

    # создание очереди ввиде списка,очередь имеет имя
    def __init__(self, name):
        self.queue = []
        self.name = name

    # создание задачи и добавление ее в очередь
    def add_task(self, task):
        return self.queue.insert(0, task)

    # взятие задачи первой в очереди
    def pop_task(self):
        return self.queue.pop()

    # перенос задачи в другую очередь
    def task_tranfer(self, queue):
        return queue.add_task(self.pop_task())

    # вывести очередь задач
    def print_task_queue(self):
        print(self.queue)

    # вывести имя очереди задач
    def print_name_queue(self):
        print(self.name)

    # решить задачу первую в очереди
    def solve_task(self):
        return TasksQueue.lst_solve_task.append(self.pop_task())


if __name__ == '__main__':
    # создать очередь
    a = TasksQueue("Базовая очередь")
    b = TasksQueue("Очередь на доработку")
    # вывести имя очереди
    a.print_name_queue()

    a.add_task('выполнить домашнее задание')
    a.add_task('помыть посуду')
    a.add_task('написать курсовую')
    a.add_task('почитать книгу')
    # вывести последовательность задач базовой очереди
    a.print_task_queue()
    # переместить задачу из базовой очереди в очередь на доработку
    a.task_tranfer(b)
    # показать очередь на доработку
    b.print_task_queue()
    # показать базовую очередь
    a.print_task_queue()
    # решить задачу из очереди на доработку
    b.solve_task()
    # посмотреть очередь на доработку
    b.print_task_queue()
    # посмотреть список решенных задач
    TasksQueue.print_lst_solve_task()
