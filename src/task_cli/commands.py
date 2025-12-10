from .task import Task
from . import db


def create_task(title):
    task = Task(title=title)
    db.save_task(task)
    print(f"Task {task} is created.")


def delete_task(task_id):
    task = db.get_task(task_id)
    task.delete()
    db.save_task(task)
    print(f"Task {task} is deleted.")


def update_task(task_id, title):
    task = db.get_task(task_id)
    task.update(title)
    db.save_task(task)
    print(f"Task {task} is updated.")


def mark_task_in_progress(task_id):
    task = db.get_task(task_id)
    task.mark_in_progress()
    db.save_task(task)
    print(f"Task {task} is marked as in progress.")


def mark_task_done(task_id):
    task = db.get_task(task_id)
    task.mark_done()
    db.save_task(task)
    print(f"Task {task} is marked as done.")


def list_tasks(status='all'):
    for task in db.list_tasks():
        if task.deleted:
            continue
        if status != 'all' and task.status != status:
            continue
        print(task)
