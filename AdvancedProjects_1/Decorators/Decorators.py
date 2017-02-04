import os

def Exists(oldFunc):
    def inside(filename):
        if(os.path.exists(filename)):
            oldFunc(filename)
        else:
            print("File '" + filename + "' does not exists")
    return inside

@Exists
def outputLine(inFile):
    with open(inFile) as f:
        print(f.readlines())

outputLine("Decorators.py")
outputLine("hello.py")