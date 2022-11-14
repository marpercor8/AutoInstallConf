
import os
import signal
import sys
from os.path import expanduser

LOCAL_DIRECTORY = os.getcwd()
USER_DIRECTORY = expanduser("~")

PACKAGE_LIST = "sources/packages.txt"
CONFIG_LIST_HOMEDIR  = "sources/path_config_home.txt"
CONFIG_LIST_DIR = "sources/path_config_dir.txt"

CONFIG_LIST_DIR_SOURCE = "dotfiles/.config"
CONFIG_LIST_HOMEDIR_SOURCE ="dotfiles"
CONFIG_LIST_PYTHON = "sources/requeriments.txt"

def signal_handler(signum, frame):
    print("Are you sure stopping? [s/N]:")
    res = input()
    if res == "s" or res == "S":
        sys.exit(0)

class App:
    install = False
    load = False
    only_python = False
    only_dir = False
    only_packages = False

    def __init__(self,dicc):
        if('h' in dicc[1]):
            print_help()
            return

        if('i' in dicc[1] and 'l' in dicc[1]):
            print("ERROR")
            print_help()
            return

        if('i' in dicc[1]):
             self.install = True
        elif('l' in dicc[1]):
             self.load = True
        else:
            print("ERROR")
            print_help()
            return

        if('d' in dicc[1]):
            self.only_dir= True
        if('p' in dicc[1]):
            self.only_packages = True
        if('y' in dicc[1]):
            self.only_python = True

        if(not self.only_dir  and not self.only_python and not self.only_packages):
            self.only_dir= True
            self.only_packages = True
            self.only_python = True
        self.main()

    def main(self):
        if(self.load):
            self.load_config_user()
        if(self.install):
            self.install_config()

    def load_config_user(self):
        if(self.only_dir):
            print("Copying user dir into {}/{}\n".format(LOCAL_DIRECTORY,CONFIG_LIST_HOMEDIR_SOURCE))
            are_u("copying config files?")
            copy_config_dir_user()
            copy_config_user_homedir()
        if(self.only_packages):
            are_u("copying packages?")
            print("Copying all packages into {}\n".format(PACKAGE_LIST).upper())
            copy_all_packages()
        if(self.only_python):
            are_u("copying python libs?")
            print("Copying all python libs into {}\n".format(CONFIG_LIST_PYTHON).upper())
            copy_requeriments()
        print("Done.") 
    def install_config(self):
        if(self.only_dir):
            print("Copying all configurations files into {}".format(CONFIG_LIST_HOMEDIR).upper())
            install_config()
        if(self.only_packages):
            print("Installing all packages from {}".format(PACKAGE_LIST).upper())
            install_packages()
        if(self.only_python):
            print("Installing all python libs from {}".format(PACKAGE_LIST).upper())
            install_python_libs()
        print("Done.") 


def create_dicc(arguments):
    dicc = {}
    dicc[1]=[]
    dicc[2]=[]
    for a in arguments:
        if(str(a).startswith("--")):
            lista = dicc[2]
            lista.append(a[2:])
            dicc[2] = lista

        elif(str(a).startswith("-")):
            lista = dicc[1]
            letras = [l for l in a][1:]
            lista.extend(letras)
            dicc[1] = list(set(lista))
        else:
           print("else")
    App(dicc)

def main(arguments):
    create_dicc(arguments[1:])
    sys.exit(0)

def print_help():
    print("AUTO INSTALL CONF\n")
    print("use: python main.py [options]\n")
    print("-h: Display this")
    print("-i: Install configuration places in dotfiles")
    print("-l: Load configuration in dotfiles")
    print("\n\n")


def copy_requeriments():
    os.system("python -m pip freeze >  {}".format(CONFIG_LIST_PYTHON))

def are_u(string):
    print("Are you sure {} [s/N]".format(string))
    i = input()
    if not(i == 's' or i == 'S'):
        sys.exit()


def install_python_libs():
    are_u("installing python libs?")
    os.system("pip install -r {}".format(CONFIG_LIST_PYTHON))

def install_packages():
    are_u("installing packages?")

    with open(PACKAGE_LIST, "r") as f:
         content = f.read()
    os.system("yay -S {}".format(content.replace("\n", " ")))

def install_config():
    are_u("installing config files?")

    first_dir = "{}/{}".format(LOCAL_DIRECTORY, CONFIG_LIST_HOMEDIR_SOURCE)
    second_dir = "{}".format(USER_DIRECTORY)
    os.system("cp -Rf {}/.config {}".format(first_dir, second_dir))
    with open(CONFIG_LIST_HOMEDIR, "r") as f:
        for config in f:
            first_dir = "{}/{}/{}".format(LOCAL_DIRECTORY, CONFIG_LIST_HOMEDIR_SOURCE, config.replace("\n", ""))
            second_dir = "{}/{}".format(USER_DIRECTORY, config.replace("\n", ""))
            os.system("cp -f {} {}".format(first_dir, second_dir))

def copy_config_dir_user():


    with open(CONFIG_LIST_DIR, "r") as f:
        for config in f:
            first_dir = "{}/.config/{}".format(USER_DIRECTORY, config.replace("\n", ""))
            second_dir = "{}/{}/{}".format(LOCAL_DIRECTORY, CONFIG_LIST_DIR_SOURCE, config.replace("\n", ""))

            os.system("rm -rf {}".format(second_dir))

            os.system("cp -rf {} {}".format(first_dir, second_dir))

def copy_config_user_homedir():


    with open(CONFIG_LIST_HOMEDIR, "r") as f:
        for config in f:
            second_dir = "{}/{}/{}".format(LOCAL_DIRECTORY, CONFIG_LIST_HOMEDIR_SOURCE, config.replace("\n", ""))
            first_dir = "{}/{}".format(USER_DIRECTORY, config.replace("\n", ""))
            
            os.system("cp -f {} {}".format(first_dir, second_dir))
            
def copy_all_packages():
    os.system("pacman -Qe | awk '{print $1}'" + "> {}/{}".format(LOCAL_DIRECTORY,PACKAGE_LIST))




if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    main(sys.argv)

