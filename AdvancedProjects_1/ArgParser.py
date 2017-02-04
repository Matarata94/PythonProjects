import argparse

def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a

def Main():
    parser = argparse.ArgumentParser()
    #for mutually exclusive arguments(can choose only one argument at a time)
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-v", "--verbose", help="Complete Sentence.", action="store_true")
    group.add_argument("-q", "--quiet", help="Short Sentence.", action="store_true")
    #for getting a number from user
    parser.add_argument("num",help="Th Fibonacci number you wish to calculate: ", type=int)
    #for defining and option
    parser.add_argument("-o", "--output", help="Output result to a file.", action="store_true")

    args = parser.parse_args()
    result = fib(args.num)
    print('The '+str(args.num)+"th fib number is ",str(result))

    if args.verbose:
        print('The ' + str(args.num) + "th fib number is ", str(result))
    elif args.quiet:
        print(result)
    else:
        print("Fib("+str(args.num)+") = "+str(result))

    if args.output:
        f = open("fibonacci.txt", "a")
        f.write(str(result)+'\n')


if __name__ == '__main__':
    Main()