from task.models import Task


def tasks_to_json(queue_of_tasks: [Task, ...], fields_to_serialize=None):
    """Сериализатор списка задач"""
    if fields_to_serialize is None:
        fields_to_serialize = ['index_num', 'date_created', 'num', 'timeout']
    tasks = []
    for task in queue_of_tasks:
        d = {}
        for attr_name in fields_to_serialize:
            d[attr_name] = getattr(task, attr_name)
        tasks.append(d)
    return tasks
