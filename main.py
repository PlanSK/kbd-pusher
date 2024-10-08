import keyboard
from time import sleep
from loguru import logger

from settings import *


def command_execute():
    keyboard.press(COMMAND)
    sleep(1)
    keyboard.release(COMMAND)
    logger.debug("Iteration completed. Wait Iteration delay.")
    sleep(BETWEEN_ITERATIONS_DELAY)
    logger.debug("Delay has been expired.")


if __name__ == "__main__":
    keyboard.wait("space")
    logger.debug(
        f"Space button pushed. Switch the window. And waiting {SWITCH_TIMESTAMP} seconds."
    )
    keyboard.send("alt+tab")
    sleep(SWITCH_TIMESTAMP)
    logger.debug("Run commands.")
    if ITERATION_COUNTER > 0:
        logger.debug(f"Limited iterations ({ITERATION_COUNTER}) start.")
        for _ in range(ITERATION_COUNTER):
            command_execute()
    else:
        logger.debug("Unlimited iterations start.")
        while True:
            command_execute()
