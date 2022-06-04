#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
<<<<<<< HEAD
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
=======
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'opensource2.settings')
>>>>>>> 4add7f86a04806d8d8d332e09f8fe0a776741e67
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

<<<<<<< HEAD
  
=======

>>>>>>> 4add7f86a04806d8d8d332e09f8fe0a776741e67
if __name__ == '__main__':
    main()
