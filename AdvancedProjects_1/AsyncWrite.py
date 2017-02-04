import threading
import time

class AsyncWrite(threading.Thread):
    def __init__(self, text, out):
        threading.Thread.__init__(self)
        self.text = text
        self.out = out

    def run(self):
        f = open(self.out, "a")
        f.write(self.text + '\n')
        f.close()
        time.sleep(2)
        print("Background Writing Finished to: " + self.out)

def Main():
    message = input("Enter a string to store: " + '\n')
    background = AsyncWrite(message, 'outTxt.txt')
    background.start()
    print("The Program can continue while it writes in another thread")
    print("125 + 876 = ", 125 + 876)

    background.join()
    print("Waited until thread was complete")

if __name__ == "__main__":
    Main()