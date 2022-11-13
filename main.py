
import os
import sys
from os.path import expanduser
import signal

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


def main(arguments):
    try:
        arg = arguments[1]
    except:
        print("ERROR: Parse error, try -h")
        sys.exit()

    try:
        if(arg=="-i"):
            print("Installing configuration")
            install()
        elif(arg=="-l"):
            print("Saving configuration")
            load_config_user()
        elif(arg=="-h"):
            print_help()
        else:
            print("ERROR")
    except:
            print("ERROR: Ha ocurrido un error en el proceso")

def print_help():
    print("AUTO INSTALL CONF\n")
    print("use: python main.py [options]\n")
    print("-h: Display this")
    print("-i: Install configuration places in dotfiles")
    print("-l: Load configuration in dotfiles")
    print("\n\n")


def load_config_user():
    print("Copying user dir into {}/{}\n".format(LOCAL_DIRECTORY,CONFIG_LIST_HOMEDIR_SOURCE))
    copy_config_dir_user()
    copy_config_user_homedir()
    print("Copying all packages into {}\n".format(PACKAGE_LIST).upper())
    copy_all_packages()
    print("Copying all packages into {}\n".format(PACKAGE_LIST).upper())
    copy_requeriments()
    print("Done.") 

def copy_requeriments():
    os.system("pip list > {}".format(CONFIG_LIST_PYTHON))


def install():
    print("Copying all configurations files into {}".format(CONFIG_LIST_HOMEDIR).upper())
    install_config()
    print("Installing all packages from {}".format(PACKAGE_LIST).upper())
    install_packages()
    print("Done.") 


def install_packages():


    with open(PACKAGE_LIST, "r") as f:
         content = f.read()
    os.system("yay -S {}".format(content.replace("\n", " ")))

def install_config():
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

