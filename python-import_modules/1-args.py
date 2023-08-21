import sys

def main():
    argv = sys.argv[1:]
    num_args = len(argv)

    if num_args == 0:
        print({num_args}, "arguments.")
    elif num_args == 1:
        print({num_args}, "argument:")
    else:
        print({num_args}, "arguments:")
    for i, arg in enumerate(argv, start=1):
        print("{}: {}".format(i, arg))
    
if __name__ == "__main__":
    main()