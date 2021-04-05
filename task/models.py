from collections import deque
from datetime import datetime


class Task:
    """Задача"""
    def __init__(self, index_num, num, timeout):
        self.index_num = index_num
        self.date_created = datetime.now()
        self.num = num
        self.timeout = timeout


class Singltone:
    """Базовый класс, реализующий паттерн синглтон"""
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


class TaskQueue(Singltone):
    """
    Очередь задач

    Очередь основана на свойстве списков хранить порядок данных, новые задачи добавляются в конец списка.
    [1, 2, 3, ...]
    """

    def __init__(self):
        if not hasattr(self, 'queue'):
            self.queue = deque()  # инициализация очереди в единственном экземпляре класса
        if not hasattr(self, 'last_task_index_num'):
            self.last_task_index_num = 0  # инициализация очереди в единственном экземпляре класса

    def get_index_num_of_last_task(self):
        """Получение порядкового номера последней задачи"""
        return self.last_task_index_num

    def get_current_task(self) -> Task or None:
        """Получение первой активной задачи в очереди"""
        try:
            return self.queue[0]
        except IndexError:
            return None

    def get_tasks(self):
        return self.queue

    def add_task(self, task: Task):
        """Добавление задачи в очередь"""
        self.queue.append(task)
        self.last_task_index_num = task.index_num  # сохраняем номер последней задачи

    def remove_task(self, task: Task):
        """Удаление задачи из очереди"""
        for index, task_in_queue in enumerate(self.queue):
            if task_in_queue.index_num == task.index_num:
                del self.queue[index]
                break


class CompletedTasks(Singltone):
    def __init__(self):
        if not hasattr(self, 'completed_tasks'):
            # инициализация списка в единственном экземпляре класса без перезатирания
            self.completed_tasks: [int, ...] = []

    def append_task(self, task: Task):
        # по идее лучше обнулять поля в классе Task и оставлять только поле index_num, но в задаче указано, что
        self.completed_tasks.append(task.num)  # необходимо именно стирать задачи

    def get_tasks(self) -> [int, ...]:
        return self.completed_tasks
