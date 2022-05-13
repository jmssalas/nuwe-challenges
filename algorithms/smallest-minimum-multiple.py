"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

from primePy import primes
from collections import Counter
import math

mcm_factors = dict()
for n in range(1, 20 + 1):
    factors = primes.factors(n)
    counter = Counter(factors)
    for factor in counter:
        count = counter[factor]
        if factor not in mcm_factors or mcm_factors[factor] < count:
            mcm_factors[factor] = count

print("MCM factors", mcm_factors);
print("Smallest minimum multiple:", math.prod([ factor**mcm_factors[factor] for factor in mcm_factors ]))