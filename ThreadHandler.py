import threading
from TimeModule import TimeHandler


class MyThread(threading.Thread):
    def __init__(self, h, m, audio):
        super(MyThread, self).__init__()
        self.h = h
        self.m = m
        self.audio = audio

    def run(self):
        while True:
            TimeHandler().check_time(self.h, self.m, self.audio)