import asyncio

from task.models import TaskQueue


async def task_worker():
    """Воркер, который в фоновом режиме последовательно выполняет задачи"""
    while True:
        current_task = TaskQueue().get_current_task()
        if current_task:
            await asyncio.sleep(current_task.timeout)
            current_task.is_active = False
        else:
            await asyncio.sleep(0.01)


async def start_background_tasks(app):
    """Сборщик задач"""
    app['task_worker'] = asyncio.create_task(task_worker())
