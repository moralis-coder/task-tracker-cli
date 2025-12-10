import json
import os
from pathlib import Path
from .task import Task

DB_PATH = '.task_cli_db'

Path(DB_PATH).mkdir(parents=True, exist_ok=True)


class NotFoundError(Exception):
    pass


def task_files():
    for file in os.listdir(DB_PATH):
        if file.endswith('.task'):
            yield os.path.join(DB_PATH, file)


def get_next_task_id():
    return len(list(task_files())) + 1



def get_task(task_id):
    task_file = os.path.join(DB_PATH, f'{task_id}.task')
    if not os.path.exists(task_file):
        raise NotFoundError(f'Task with ID {task_id} not found.')
    with open(task_file, 'r') as f:
        data = json.load(f)
        return Task.from_dict(data)


def save_task(task):
    if task.id is None:
        task.id = get_next_task_id()

    task_file = os.path.join(DB_PATH, f'{task.id}.task')
    with open(task_file, 'w') as f:
        json.dump(task.__dict__(), f)


def list_tasks():
    for task_id in range(1, get_next_task_id()):
        try:
            with open(os.path.join(DB_PATH, f'{task_id}.task'), 'r') as f:
                data = json.load(f)
                yield Task.from_dict(data)
        except FileNotFoundError:
            continue    
