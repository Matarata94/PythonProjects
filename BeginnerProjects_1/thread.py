import threading

class MataMessenger(threading.Thread):
    def run(self):
        for _ in range(10):
            print(threading.currentThread().getName())

x = MataMessenger(name='Send Message')
y = MataMessenger(name='Recieve Message')
x.start()
y.start()