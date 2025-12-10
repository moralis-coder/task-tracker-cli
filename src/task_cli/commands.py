from .task import Task
from . import db


def create_task(title):
    task = Task(title=title)
    db.save_task(task)


def delete_task(task_id):
    task = db.get_task(task_id)
    task.delete()
    db.save_task(task)
    print(f"Task {task} is deleted.")
