import keyboard
from time import sleep
from loguru import logger

ITERATION_COUNTER = 1
COMMAND = "enter"


def command_execute():
    keyboard.write("ls")
    keyboard.press(COMMAND)
    sleep(10)
    logger.debug("commands executed.")


if __name__ == "__main__":
    keyboard.wait("space")
    logger.debug("Space button pushed.")
    keyboard.send("alt+tab")
    sleep(2)
    if ITERATION_COUNTER > 0:
        for _ in range(ITERATION_COUNTER):
            command_execute()
    else:
        while True:
            command_execute()
