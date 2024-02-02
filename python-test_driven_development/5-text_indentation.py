#!/usr/bin/python3
"""Module: 5-text_indentation"""
def text_indentation(text):
    """text - text must be a string"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    i = 0
    while i < len(text):
        print(text[i], end='')
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            print('\n')
            if i + 1 < len(text) and text[i + 1] == ' ':
                i += 1
