import re

def Main():
    line = "I Think i understand regular expressions"
    matchResult = re.match('think',line,re.M|re.I)
    if matchResult:
        print("Founded By 're.match()' : "+matchResult.group())
    else:
        print("Not Founded By 're.match()' ")

    searchResult = re.search('think',line,re.M|re.I)
    if searchResult:
        print("Search Found: "+searchResult.group())
    else:
        print("Nothing found in search")

if __name__ == '__main__':
    Main()