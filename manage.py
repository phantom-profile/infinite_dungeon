import sys

import launcher.initialize  # noqa

COMMANDS = [
    "makemigrations",
    "migrate",
    "shell_plus"
]


def main():
    """Run administrative tasks."""
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    if len(sys.argv) > 1 and sys.argv[1] not in COMMANDS:
        raise NotImplementedError(f"unknown command {sys.argv[1]}")
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
