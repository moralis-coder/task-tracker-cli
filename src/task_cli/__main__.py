from . import cli
from . import commands
from . import db
from . import task


COMMANDS = {
    'add': lambda **kwargs: commands.create_task(kwargs['task_name']),
    'delete': lambda **kwargs: commands.delete_task(kwargs['task_id']),
    'update': lambda **kwargs: commands.update_task(kwargs['task_id'], kwargs['task_name']),
    'mark-in-progress': lambda **kwargs: commands.mark_task_in_progress(kwargs['task_id']),
    'mark-done': lambda **kwargs: commands.mark_task_done(kwargs['task_id']),
}


def main():
    args = cli.parse_args()
    command = COMMANDS.get(args.command, lambda **kwargs: print(f'Command {args.command} is not implemented yet.'))
    
    try:
        command(**vars(args))
    except db.NotFoundError as e:
        print(e)
    except task.InvalidTaskArgument as e:
        print(f'Invalid task operation: {e}')


if __name__ == "__main__":
    main()
