#!/usr/local/bin/python3

'''
Write a generator function that generates progressively more accurate approximations of the Leibniz formula for π.

According to wiki, in mathematics, the Leibniz formula for π, named after Gottfried Leibniz , states that

    1 - 1/3 + 1/5 - 1/7 + 1/9 - ... = π/4

'''

import math
import time

# This generator yields the Leibniz series, which is the left-hand side of
# the formula and when a value is sent to it, set n to that value
def leibniz():
    n = 0
    while True:
        n = yield math.pow(-1,n)/(2*n + 1)

# initialization
pi = leibniz()
pi.send(None)
result = 0
n = 0

while True:

    # result represents the right-hand side of the formula, which is π/4
    # it's the sum of the Leibniz series
    result += pi.send(n)
    n += 1

    # print out the approximation of π
    print(result*4, "\t<<< This is an infinite loop. Press Ctrl-C to end it!")

    # just need some time to see how the number changes
    time.sleep(0.5)

