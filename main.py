from aiohttp import web
from task.routes import setup_routes
from task.background_tasks import start_background_tasks

app = web.Application()
setup_routes(app)
app.on_startup.append(start_background_tasks)
web.run_app(app)
