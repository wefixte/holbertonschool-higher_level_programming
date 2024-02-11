#!/usr/bin/python3

""" Function that adds 2 newlines after each of these characters: . ? and : """


def text_indentation(text):
    """
    Adds 2 newlines after these char : ".?:"
    Args:
        text (string): text to modify and to print
    Raises:
        TypeError: if text is not a string
    """

    # Check if arguments are corrects
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Loop to add new lignes
    for ponctuation in ".?:":
        text = (ponctuation + "\n\n").join(
            [line.strip(" ") for line in text.split(ponctuation)])

    # Print text
    print("{}".format(text), end="")
