# thanks to https://groups.google.com/g/kivy-users/c/0M9uaXCC8XA/m/UZd-koocmFsJ


import logging
import time

from kivy import Logger


class LoggerWithTime:

    def __init__(self):
        self.emit_org = None

        # we create a formatter object once to avoid
        # inialisation on every log line
        self.oFormatter = logging.Formatter(None)

        # we just need to patch the first Handler
        # as we change the message itself
        oHandler = Logger.handlers[0]
        self.emit_org = oHandler.emit
        oHandler.emit = self.emit

    def emit(self, record):
        # we do not use the formatter by purpose as it runs on failure
        # if the message string contains format characters

        t = str(int(record.msecs))

        msg = record.msg.split(':', 1)
        if len(msg) == 2:
            record.msg = msg[0] + ": [" + t + "] " + msg[1]

        else:
            record.msg = "[" + t + "] " + record.msg

        self.emit_org(record)


loggerWithTime = LoggerWithTime()
