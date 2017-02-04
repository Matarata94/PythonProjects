import threading
import time

tlock = threading.Lock()
def timer(name, delan, repeat):
    print("Timer: " + name + " Started")
    tlock.acquire()
    print(name + " has acquired the lock")
    while repeat > 0:
        time.sleep(delan)
        print(name + ": " + str(time.ctime(time.time())))
        repeat -= 1
    print(name + " is releasing the lock")
    tlock.release()
    print("Timer: " + name + " Completed")

def Main():
    t1 = threading.Thread(target=timer, args=("Timer1", 1, 5))
    t2 = threading.Thread(target=timer, args=("Timer2", 1.5, 5))
    t1.start()
    t2.start()
    print("Main Completed")

if __name__ == "__main__":
    Main()