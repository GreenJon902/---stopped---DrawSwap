import datetime
import logging
import sys


class TimeFormatter(logging.Formatter):
    converter = datetime.datetime.fromtimestamp
    begin_time = datetime.datetime.now().strftime("%s")

    def formatTime(self, record, datefmt=None):
        ct = self.converter(record.created)
        if datefmt:
            s = ct.strftime(datefmt)
            dSecs = int(s[:-7]) - int(self.begin_time)
            aSecs = str(s[:-7])[-2:]
            msecs = s[-6:-3]
            s = str(dSecs) + " | " + str(aSecs) + " " + msecs
        else:
            t = ct.strftime("%Y-%m-%d %H:%M:%S")
            s = "%s,%03d" % (t, record.msecs)
        return s


logFormatter = TimeFormatter("[%(threadName)-12.12s] [%(levelname)-7s] [%(name)-10s] [%(asctime)s]  %(message)s",
                             datefmt='%s %f')
rootLogger = logging.getLogger()
rootLogger.setLevel(logging.DEBUG)

fileHandler = logging.FileHandler("{0}/{1}.log".format("./", "latest"))
fileHandler.setFormatter(logFormatter)
rootLogger.addHandler(fileHandler)

consoleHandler = logging.StreamHandler(sys.stdout)
consoleHandler.setFormatter(logFormatter)
rootLogger.addHandler(consoleHandler)

rootLogger.info("Setup Logger")
