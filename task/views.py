import json

from aiohttp import web

from .models import TaskQueue, CompletedTasks
from .serializers import tasks_to_json
from .services import add_task
from .validators import json_parse_exception


async def get_active_tasks(request):
    task_queue = TaskQueue()
    tasks = task_queue.get_tasks()
    data = tasks_to_json(tasks)
    return web.Response(text=data, status=200)


@json_parse_exception
async def create_task(request):
    data = await request.json()
    add_task(data)
    return web.Response(text='detail: created', status=201)


async def get_completed_tasks(request):
    completed_tasks = CompletedTasks()
    tasks = completed_tasks.get_tasks()
    return web.Response(text=json.dumps(tasks, indent=4, sort_keys=True, default=str), status=200)
