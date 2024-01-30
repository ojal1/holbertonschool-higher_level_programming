#!/usr/bin/python3
def roman_to_int(roman_string):
    result = 0
    value_prev = 0
    roman_dict = {
        'I': 1,
        'V': 5, 
        'X': 10, 
        'L': 50, 
        'C': 100, 
        'D': 500, 
        'M': 1000}
    if not isinstance(roman_string, str):
        return result
    for letter in roman_string:
        value = roman_dict.get(letter, 0)
        if value == 0:
            return 0
        if 0 < value_prev < value:
            result += value - value_prev * 2
        else:
            value_prev = value
            result += value
    return result
