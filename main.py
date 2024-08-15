import keyboard
from time import sleep
from loguru import logger
from dotenv import load_dotenv
import os

from settings import *


def command_execute(command: str, delay: int, command_delay: int = 1) -> None:
    keyboard.press(command)
    sleep(command_delay)
    keyboard.release(command)
    logger.debug("Iteration completed. Wait Iteration delay.")
    sleep(delay)
    logger.debug("Delay has been expired.")


if __name__ == "__main__":
    load_dotenv()
    try:
        start_commdand = os.getenv("START_COMMAND")
        iteration_counter = int(os.getenv("ITERATION_COUNTER", "1"))
    except AssertionError:
        logger.error("Error of type checking in ENV section.")
        raise
    # Message with counter must be added.
    print(f"Iteration counter set to {iteration_counter}.")
    print(f"Please push '{start_commdand}' button to start.")
    keyboard.wait(start_commdand)
    logger.debug(
        f"Space button pushed. Switch the window. And waiting {SWITCH_TIMESTAMP} seconds."
    )
    keyboard.send("alt+tab")
    sleep(SWITCH_TIMESTAMP)
    logger.debug("Run commands.")

    if iteration_counter > 0:
        logger.debug(f"Limited iterations ({iteration_counter}) start.")
        for _ in range(iteration_counter):
            command_execute(COMMAND, BETWEEN_ITERATIONS_DELAY)
    else:
        logger.debug("Unlimited iterations start.")
        while True:
            command_execute(COMMAND, BETWEEN_ITERATIONS_DELAY)
