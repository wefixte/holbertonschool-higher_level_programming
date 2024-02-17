#!/usr/bin/python3
""" Read texte files """


def read_file(filename=""):
    """ Reading texte file function """
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
