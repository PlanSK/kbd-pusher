import keyboard
from time import sleep


if __name__ == "__main__":
    keyboard.wait('space')
    keyboard.send('alt+tab')
    sleep(2)
    keyboard.write('ls')
    keyboard.press('enter')
    print('Space key pushed.')
