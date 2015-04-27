__author__ = 'hannes'

import itertools
import math

n = 6

print(math.factorial(n))
for r in itertools.permutations(range(1, 1 + n)):
    print(str(r).strip('()').replace(",", ""))