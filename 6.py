#!/usr/bin/python3

str1 = "this is really a string example....wow!!! is"
str2 = "is"

print(str1.rfind(str2))

print(str1.rfind(str2, 0, 10))
print(str1.rfind(str2, 10, 0))