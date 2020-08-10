import sys

a = "111"

print(sys.getrefcount(a))

b = a

print(sys.getrefcount(a))