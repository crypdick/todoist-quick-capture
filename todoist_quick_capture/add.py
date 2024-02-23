from todoist_api_python.api import Task, TodoistAPI


def add_task(text: str, token: str) -> str:
    """Add a task to Todoist."""
    api = TodoistAPI(token)

    print(f"Raw submission: {text}")
    task: Task = api.quick_add_task(text=text)
    print(task)

    return task
