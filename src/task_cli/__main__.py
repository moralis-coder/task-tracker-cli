from . import cli
from . import commands


COMMANDS = {
    'add': lambda **kwargs: commands.create_task(kwargs['task_name']),
}


def main():
    args = cli.parse_args()
    command = COMMANDS.get(args.command, lambda **kwargs: print(f'Command {args.command} is not implemented yet.'))
    command(**vars(args))


if __name__ == "__main__":
    main()
