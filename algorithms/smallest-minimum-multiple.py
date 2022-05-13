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