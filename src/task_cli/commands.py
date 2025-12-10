from .task import Task
from .db import save_task

def create_task(title):
    task = Task(title=title)
    save_task(task)
