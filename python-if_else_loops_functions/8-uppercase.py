#!/usr/bin/python3
define uppercase(str):
for i in str:
    if 97 >= ord(i) <= 122:
        i = chr(i - 32)
        print({}.format(i))
