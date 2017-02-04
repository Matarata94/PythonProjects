msg = "hello"

def myStr(s):
    while len(s) != 0:
        print(s)
        s = s[1:]

myStr(msg)