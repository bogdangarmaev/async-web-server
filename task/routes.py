from .views import get_active_tasks, get_unactive_tasks, create_task


def setup_routes(app):
    app.router.add_post('/task', create_task)
    app.router.add_get('/task_queue', get_active_tasks)
    app.router.add_get('/result', get_unactive_tasks)
