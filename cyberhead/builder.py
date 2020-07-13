import yaml
from shutil import rmtree, copytree
from os import path, system


def read_compose(file):
    with open(file) as compose_file:
        compose = yaml.load(compose_file, Loader=yaml.FullLoader)
        return compose


def copy_folder(source, destination):
    if path.exists(destination):
        rmtree(destination)
    copytree(source, destination)
    print(f'[COPIED] from:{source} to:{destination}')


def transfer_modules(modules):
    for module_key, module in modules.items():
        source = module['dir']
        destination = f'/app/cyberhead/{module_key}'
        copy_folder(source, destination)

        for submodule_key, submodule in module.items():
            if submodule_key != 'dir':
                source = submodule['dir']
                destination = f'/app/cyberhead/{module_key}/{submodule_key}'
                copy_folder(source, destination)


def build(file):
    compose = read_compose(file)
    transfer_modules(compose['modules'])
    system('pip3 install .')
    # system('pip3 install -r /app/cyberhead/requirements.txt')


if __name__=="__main__":
    build('/app/cyberhead-compose.yml')
