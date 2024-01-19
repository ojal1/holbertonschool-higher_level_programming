#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if 0 < number:
    print(f"{number} is positive")
if 0 == number:
    print(f"{number} is zero")
if 0 > number:
    print(f"{number} is negative")
