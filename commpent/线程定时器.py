import threading
#
class LoopTimer(threading._Timer):
    def __init__(self,interval,function,args = [], kwargs = {}):
        threading._Timer.__init__(self,interval, function, args, kwargs)

    def run(self):
        while True:
            self.finished.wait(self.interval)
            if self.finished.is_set():
                self.finished.set()
                break
            self.function(*self.args, **self.kwargs)