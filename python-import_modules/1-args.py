import sys

def main():
    arguments = sys.argv[1:]
    num_arguments = len(arguments)

    print("Number of argument{}: {}{}".format(
        's' if num_arguments != 1 else '', num_arguments,
        '' if num_arguments == 0 else ':'))

    if num_arguments > 0:
        for i, arg in enumerate(arguments, start=1):
            print("{}: {}".format(i, arg))

if __name__ == "__main__":
    main()

import sys

# The number of arguments passed 
num_args = len(sys.argv) - 1

# Print the number of arguments
print(f"Number of argument(s): {num_args}")

if num_args == 0:
    print(".")
else:
    # Print "argument" if there's only one argument, otherwise "arguments"
    plural = "argument" if num_args == 1 else "arguments"
    print(f"{plural}:")

    # Print each argument along with its position
    for i in range(1, len(sys.argv)):
        print(f"{i}: {sys.argv[i]}")
