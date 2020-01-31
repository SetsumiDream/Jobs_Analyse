import os
import time
import multiprocessing
from logging.handlers import TimedRotatingFileHandler
from logging import FileHandler

lock = multiprocessing.Lock()


class SafeLog(TimedRotatingFileHandler):
    def __init__(self, *args, **kwargs):
        super(SafeLog, self).__init__(*args, **kwargs)
        self.suffix_time = ""
        self.origin_basename = self.baseFilename


    def shouldRollover(self, record):
        timeTuple = time.localtime()
        if self.suffix_time != time.strftime(self.suffix, timeTuple) or not os.path.exists(self.origin_basename+'.'+self.suffix_time):
            return 1
        else:
            return 0

    def doRollover(self):
        if self.stream:
            self.stream.close()
            self.stream = None

        currentTimeTuple = time.localtime()
        self.suffix_time = time.strftime(self.suffix, currentTimeTuple)
        self.baseFilename = self.origin_basename + '.' + self.suffix_time

        self.mode = 'a'

        global lock
        with lock:
            if self.backupCount > 0:
                for s in self.getFilesToDelete():
                    os.remove(s)

        if not self.delay:
            self.stream = self._open()

    def getFilesToDelete(self):
        #将源代码的 self.baseFilename 改为 self.origin_basename
        dirName, baseName = os.path.split(self.origin_basename)
        fileNames = os.listdir(dirName)
        result = []
        prefix = baseName + "."
        plen = len(prefix)
        for fileName in fileNames:
            if fileName[:plen] == prefix:
                suffix = fileName[plen:]
                if self.extMatch.match(suffix):
                    result.append(os.path.join(dirName, fileName))
        if len(result) < self.backupCount:
            result = []
        else:
            result.sort()
            result = result[:len(result) - self.backupCount]
        return result