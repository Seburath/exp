from sys import argv
from os import system


def update():
    '''reinstall the wrapper outside the container'''
    system('pipx install . --force')


def enter():
    '''open a terminal into the container'''
    system('docker-compose exec cyberhead bash')


def build():
    '''erase modules and build the package'''
    update()
    system('docker-compose exec cyberhead python3 '
           '/app/cyberhead/builder.py')


def dev():
    '''start the developer mode'''
    build()
    system('docker-compose exec cyberhead '
           'python3 /app/cyberhead/core/tasker.py')


def cli():
    cmd = argv[1]
    if cmd == 'update':
        update()
    elif cmd == 'build':
        build()
    elif cmd == 'enter':
        enter()
    elif cmd == 'dev':
        dev()
    elif cmd == '--help' or cmd == '-h' or cmd == 'help':
        print('no written help yet, read the wrapper.py from core')
    else:
        print('Command not found, use --help for the commands list')
