#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    print('  /\\   /\\                        _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _')
    print(' //\\\_//\\\\        ____         /                                   \\')
    print(' \\_     _/       /   /        /       Aguará Technologies           \\')
    print('  /  * * \\      /^^^]    < ====   Chaco - Argentina , Bienvenido =) |')
    print('  \\_ \\0/_/     [   ]          \\      == SGA CET - UTN FRRe ==       /')
    print('    /    \\_    [  /            \\ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ /')
    print('    \\      \\_  / /')
    print('     [ [ /   \\/_/')
    print('    _[ [ \\   /_/')
    print('')
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sga_cet.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
