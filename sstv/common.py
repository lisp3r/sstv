"""Shared methods"""

from os import get_terminal_size
from sys import stderr, stdout, platform
import logging


logging.basicConfig(format='[%(name)s]    %(message)s', level=logging.INFO)
log = logging.getLogger('sstv')


def progress_bar(progress, complete, message="", show=True):
    """Simple loading bar"""

    if not show:
        return

    message_size = len(message) + 7  # prefix size
    cols = 100
    percent_on = True
    level = progress / complete
    bar_size = min(cols - message_size - 10, 100)
    bar = ""

    if bar_size > 5:
        fill_size = round(bar_size * level)
        bar = "[{}]".format(''.join(['#' * fill_size,
                                     '.' * (bar_size - fill_size)]))
    elif bar_size < -3:
        percent_on = False

    percent = ""
    if percent_on:
        percent = "{:4d}%".format(int(level * 100))

    align = cols - message_size - len(percent)
    log.info("{}{:>{width}}{}".format(message, bar, percent, width=align))
