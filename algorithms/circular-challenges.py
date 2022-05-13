"""
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""

import functools
from primePy import primes
from collections import deque

limit = 1000000

circular_primes = list()
for n in range(2, limit):
    if primes.check(n):
        digits = [ d for d in str(n) ]
        circular = True
        deque_obj = deque(digits)
        for rotation in range(1, len(digits)):
            deque_obj.rotate()
            rotated = functools.reduce(lambda x, y: x + y, deque_obj)
            circular = circular and primes.check(int(rotated))
        if circular:
            circular_primes.append(n)

print("Circular primes", circular_primes)
print("Total circular primes:", len(circular_primes))