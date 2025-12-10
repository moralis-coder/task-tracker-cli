import argparse


def parse_args():
    parser = argparse.ArgumentParser(
        prog="task-cli",
        description="A command-line tool to manage your tasks.",
    )

    subparser = parser.add_subparsers(dest='command', required=True)

    add_subcommand = subparser.add_parser('add', description='Add a new task')
    add_subcommand.add_argument('task_name', type=str, help='Name of the task to add')

    update_subcommand = subparser.add_parser('update', description='Update an existing task')
    update_subcommand.add_argument('task_id', type=int, help='ID of the task to update')
    update_subcommand.add_argument('new_name', type=str, help='New name for the task')

    delete_subcommand = subparser.add_parser('delete', description='Delete a task')
    delete_subcommand.add_argument('task_id', type=int, help='ID of the task to delete')

    mark_in_progress_subcommand = subparser.add_parser('mark-in-progress', description='Mark a task as in progress')
    mark_in_progress_subcommand.add_argument('task_id', type=int, help='ID of the task to mark as in progress')

    mark_done_subcommand = subparser.add_parser('mark-done', description='Mark a task as done')
    mark_done_subcommand.add_argument('task_id', type=int, help='ID of the task to mark as done')

    list_subcommand = subparser.add_parser('list', description='List all tasks')
    list_subcommand.add_argument('status', nargs='?', default='all', choices=['all', 'todo', 'in-progress', 'done'], help='Filter tasks by status')

    return parser.parse_args()
