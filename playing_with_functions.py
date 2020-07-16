#!/usr/bin/env python3
"""
Here is the docstring
"""

A = 7
print(isinstance(A, int))

def add_2_nums():
    """
    This adds 2 numbers together
    """
    ax = 5
    ay = 3
    result = ax + ay
    return result
    #return "poodle"

print(add_2_nums())


def mult_2_nums(j, k):
    result = j * k
    return result


print(mult_2_nums(7, 4))


for num in range(1, 5):
    print(mult_2_nums(num, 2))


def complex_math():
    mult_res = mult_2_nums(12, 6)
    print(mult_2_nums(mult_res, 3))


complex_math()


def default_math(num1, num2=5):
    return num1 - num2


# One required positional argument
print(default_math(4, 9))


# def <func_name>(required_pos_args, optional_args):
def switchy_text(txt1="mine", txt2="yours"):
    print(txt1[-1::-1])
    print(txt2[-1::-1])


switchy_text()
switchy_text(txt2="his", txt1="hers")
