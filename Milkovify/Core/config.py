import inspect
from typing import Union
from datetime import datetime

from colorama import Fore, Style, init
import asyncio


from colorama import Fore, Back, Style


class BotLogging:
    def __init__(
        self,
        bot_name: str,
    ):
        ##f=logging.Formatter('%(asctime)s :: %(module)s :: %(levelname)s :: %(message)s',datefmt='%d-%b-%y %H:%M:%S')
        self.level = "WARNING"
        self.levels = ["DEBUG", "INFO", "GENERAL", "WARNING", "CRITICAL"]

    def set_level(self, level: Union[str, int]):
        if level in self.levels:
            self.level = level
            return self.GENERAL("Logging level set to {0}".format(self.level))

        elif isinstance(level, int):
            if level < len(self.levels) + 1:
                self.level = self.levels[level]
                return self.GENERAL("Logging level set to {0}".format(self.level))
            return self.CRITICAL("{0} is out of range for level".format(level))

        return self.CRITICAL("Setting level to {0} Failed".format(level))

    def check_level(self, level):
        return self.levels.index(self.level) - self.levels.index(level) < 1


    def _log(
        self,
        color,
        level,
        msg,
    ):

        if not self.check_level(level):
            return
        asctime = datetime.now()
        time_string = asctime.strftime("%d-%b-%y %H:%M:%S")
        string_formatted = "|| ".join([time_string, level, msg])
        print(color + string_formatted)

        print(Style.RESET_ALL)

    def DEBUG(self, msg: str, clr=Fore.YELLOW):
        self._log(clr, "DEBUG", msg)

    def INFO(self, msg: str, clr=Fore.GREEN):
        self._log(clr, "INFO", msg)

    def GENERAL(self, msg: str, clr=Fore.CYAN):
        self._log(clr, "GENERAL", msg)

    def WARNING(self, msg: str, clr=Fore.RED):
        self._log(clr, "WARNING", msg)

    def CRITICAL(self, msg: str, clr=Fore.RED):
        self._log(clr, "CRITICAL", msg)


logger = BotLogging("Milkbot")
github = "None"
VERSION = "0.0.1"
TOKEN = ""
PREFIX = "~"
AUTHOR = "Florence"
USER_ID = ""
DESCRIPTION = """"""
