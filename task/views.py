import json

from aiohttp import web

from .models import TaskQueue
from .serializers import tasks_to_json
from .services import add_task
from .validators import json_parse_exception


async def get_active_tasks(request):
    tasks = TaskQueue().get_filtered_tasks(is_active=True)
    data = tasks_to_json(tasks)
    return web.Response(text=json.dumps(data, indent=4, sort_keys=True, default=str), status=200)


@json_parse_exception
async def create_task(request):
    data = await request.json()
    add_task(data)
    return web.Response(text='detail: created', status=201)


async def get_unactive_tasks(request):
    tasks = TaskQueue().get_filtered_tasks(is_active=False)
    data = tasks_to_json(tasks, fields_to_serialize=('num',))
    return web.Response(text=json.dumps(data, indent=4, sort_keys=True, default=str), status=200)
