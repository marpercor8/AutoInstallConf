# AutoInstallConf

Little script for copy your data and config files

## Dependencies
| Dependency | Description |
|----------|:-------------:|
|Python 3.X | Main script|
|yay    | Install all packages even if is a aur package|
|pacman | Query for all packages|


## Usage

| Value | Description |
|----------|:-------------:|
|`-h`| Display this section |
|`-i`| Copy dotfiles dir into your home directory and install all packages from packages.txt |
|`-l`| Copy your dotfiles into this dir and copy packages into packages.txt |

Example:
```
 ./main.py -i 
```
