import asyncio

from task.models import TaskQueue, CompletedTasks


async def task_worker():
    """Воркер, который в фоновом режиме последовательно выполняет задачи"""
    while True:
        task_queue = TaskQueue()
        completed_tasks = CompletedTasks()
        current_task = task_queue.get_current_task()
        if current_task:
            await asyncio.sleep(current_task.timeout)
            task_queue.remove_task(current_task)
            completed_tasks.append_task(current_task)
        else:
            await asyncio.sleep(0.01)  # передаем управление обратно в событийный цикл если задач нет


async def start_background_tasks(app):
    """Сборщик задач"""
    app['task_worker'] = asyncio.create_task(task_worker())
