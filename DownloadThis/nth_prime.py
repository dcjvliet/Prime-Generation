from math import log, e, floor, ceil
from segmented_sieve import segmentedSieve


def bounds(n):
    ln = log(n, e)
    lower_bound = n * (ln + log(ln, e) - 1)
    upper_bound = n * (ln + log(ln, e))
    return floor(lower_bound), ceil(upper_bound)


def nth_prime(n):
    lower, upper = bounds(n)
    return segmentedSieve(lower, upper)

