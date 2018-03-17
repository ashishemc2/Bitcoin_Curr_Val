import time
class Fetch_time:
    def currentTime(self):
        curr_time = time.strftime("%H:%M:%S", time.localtime())
        return curr_time

    @classmethod
    def sleep(cls,dur):
        time.sleep(dur)