#!/usr/bin/env python3

# Created by Cristiano Sellitto
# Created in October 2022
# A program that finds the sum of two user inputted numbers

import math


def main():
    # Finds the sum of two numbers the user sends

    first_number = float(input("Enter first number to add: "))
    second_number = float(input("Enter second number to add: "))
    sum = first_number + second_number
    print("\n{0} + {1} = {2}".format(first_number, second_number, sum))

    print("\nDone.")


if __name__ == "__main__":
    main()
