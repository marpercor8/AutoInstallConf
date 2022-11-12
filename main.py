
import os
import sys
from os.path import expanduser


LOCAL_DIRECTORY = os.getcwd()
USER_DIRECTORY = expanduser("~")

PACKAGE_LIST = "source/packages.txt"
CONFIG_LIST_DIR = "path_config_dir.txt"
CONFIG_LIST_DIR_SOURCE = "source/config_user"
CONFIG_LIST_HOMEDIR  = "path_config_home.txt"
CONFIG_LIST_HOMEDIR_SOURCE ="source/main_config"
def main():
    pass


def install_packages():
  with open(PACKAGE_LIST, "r") as f:
        for l in f:
            os.system("trizen -Syua {}".format(l))


def load_config_user():
    pass

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
    main()
    

