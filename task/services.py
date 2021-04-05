from task.models import TaskQueue, Task
from task.validators import str_to_int


def add_task(data: dict):
    """Добавить задачу в очередь"""
    num = str_to_int(data, 'num')
    timeout = str_to_int(data, 'timeout')
    tq = TaskQueue()
    index_num_of_last_task = tq.get_index_num_of_last_task()
    task = Task(index_num_of_last_task + 1, num, timeout)
    tq.add_task(task)
