#import add function from mypackage
from mypackage.add_0 import add
a = 1
b = 2
#perform the addition using format style
print("{} + {} = {}" .format(a, b, add(a, b)))