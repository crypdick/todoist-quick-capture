from todoist_api_python.api import Task, TodoistAPI


def add_task(text: str, token: str) -> Task:
    """
    Add a task to Todoist.

    Args:
        text (str): The text of the task.
        token (str): The Todoist API token.

    Returns:
        Task: The ID of the newly created task.
    """
    assert text, "Task text cannot be empty"
    api = TodoistAPI(token)

    print(f"Raw submission: {text}")
    task: Task = api.quick_add_task(text=text)
    print(task)

    # TODO: unsure how to check for 400 errors

    return task
