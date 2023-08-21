#import add function from mypackage
from mypackage.add_0 import add

def main():
    a = 1
    b = 2
    # Perform the addition using format style
    print("{} + {} = {}".format(a, b, add(a, b)))

if __name__ == "__main__":
    main()