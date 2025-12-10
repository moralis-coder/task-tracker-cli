import json
import os
from pathlib import Path
from .task import Task

DB_PATH = '.task_cli_db'

Path(DB_PATH).mkdir(parents=True, exist_ok=True)

def task_files():
    for file in os.listdir(DB_PATH):
        if file.endswith('.task'):
            yield os.path.join(DB_PATH, file)

def get_next_task_id():
    return len(list(task_files())) + 1


def save_task(task):
    if task.id is None:
        task.id = get_next_task_id()

    task_file = os.path.join(DB_PATH, f'{task.id}.task')
    with open(task_file, 'w') as f:
        json.dump(task.__dict__(), f)
