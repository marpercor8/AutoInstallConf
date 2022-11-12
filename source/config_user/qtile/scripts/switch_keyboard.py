import os
 
def change_keyboard():
    layout = os.popen('setxkbmap -query | grep layout').read()
    layout = layout.strip().split(' ')[-1]
    if layout == 'es':
        os.system('setxkbmap us')
    else:
        os.system('setxkbmap es')
    return layout


if __name__ == "__main__":
    change_keyboard()