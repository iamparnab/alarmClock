import time
import sys


class TimeHandler:

    def check_time(cls, h, m, audio):
        current_time = time.localtime()
        if current_time.tm_hour is h and current_time.tm_min is m:
            audio.play()
            sys.exit()