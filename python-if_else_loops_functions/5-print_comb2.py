#!/usr/bin/python3
for index in range(100):
    print("{:02d}".format(index), end=", " if index < 99 else "\n")
