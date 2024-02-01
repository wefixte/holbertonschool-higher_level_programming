#!/usr/bin/python3
# Function to change a letter to an integer
def roman_to_int(roman_string):
    # Check if the input is valid
    if roman_string is None or type(roman_string) is not str:
        return 0

    # Dictionary to map Roman numerals to their integer values
    roman_numeral = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                     'C': 100, 'D': 500, 'M': 1000}
    result = 0

    # Iterate until len - 1 to avoid IndexError
    for index in range(len(roman_string) - 1):
        # Get the integer value of the current and next Roman numeral
        value = roman_numeral[roman_string[index]]
        next_value = roman_numeral[roman_string[index + 1]]

        # Compare the current and next value to determine if we add or subtract
        if value >= next_value:
            result += value
        else:
            result -= value

    # Add the value of the last character (no next to compare with)
    result += roman_numeral[roman_string[-1]]
    return result
