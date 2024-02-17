#!/usr/bin/python3
""" Write a string to a texte file, return number of characters written """


def write_file(filename="", text=""):
    """ Function that writes a string to a texte file """
    with open(filename, 'w', encoding="utf-8") as file:
        return file.write(text)
