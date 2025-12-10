from . import cli


def main():
    args = cli.parse_args()
    print(args)


if __name__ == "__main__":
    main()
