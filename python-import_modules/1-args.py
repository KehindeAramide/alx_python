import sys

def main():
    argv = sys.argv[1:]
    num_args = len(argv)

    if num_args == 0:
        print ("Number of arg(s) .")
    elif num_args == 1:
        print("Number of argument(s) argument:")
    else:
        print("Number of argument(s) arguments:")
    for i, arg in enumerate(argv, start=1):
        print("{}: {}".format(i, arg))
    
if __name__ == "__main__":
    main()