from task.models import TaskQueue
from task.validators import str_to_int


def add_task(data: dict):
    """Добавить задачу в очередь"""
    num = str_to_int(data, 'num')
    timeout = str_to_int(data, 'timeout')
    tq = TaskQueue()
    tq.add_task(num, timeout)
