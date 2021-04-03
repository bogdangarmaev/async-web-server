from collections import deque
from datetime import datetime


class Task:
    """Задача"""
    def __init__(self, index_num, num, timeout):
        self.index_num = index_num
        self.date_created = datetime.now()
        self.num = num
        self.timeout = timeout
        self.is_active = True


class TaskQueue:
    """
    Очередь задач

    Очередь основана на свойстве списков хранить порядок данных, новые задачи добавляются в конец списка.
    [1, 2, 3, ...]
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        """Реализуем паттерн синглтон для гарантии единственного списка во всей системе"""
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'queue'):
            self.queue = deque()  # инициализация очереди в единственном экземпляре класса

    def _get_index_num_of_last_task_(self):
        """Получение порядкового номера последней задачи"""
        try:
            last_task = self.queue[-1]
            return last_task.index_num
        except IndexError:
            return 0

    def get_filtered_tasks(self, is_active: bool) -> [Task, ...]:
        """Получение задач, отфильтрованных по активности"""
        return [task for task in self.queue if task.is_active == is_active]

    def get_current_task(self) -> Task or None:
        """Получение первой активной задачи в очереди"""
        active_tasks = self.get_filtered_tasks(is_active=True)
        try:
            return active_tasks[0]
        except IndexError:
            return None

    def add_task(self, num: int, timeout: int):
        """Добавление задачи в очередь"""
        task = Task(self._get_index_num_of_last_task_(), num, timeout)
        self.queue.append(task)
