import os
from typing import Optional

import dotenv
from todoist_api_python.api import Task, TodoistAPI

dotenv.load_dotenv()
token = os.getenv("TODOIST_API_TOKEN")
api = TodoistAPI(token)


def add_task(text: str) -> str:
    try:
        print(f"Raw submission: {text}")
        task: Task = api.quick_add_task(text=text)
        print(task)
    except Exception as error:
        print(error)

    return task
