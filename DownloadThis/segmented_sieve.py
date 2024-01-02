import math
from sympy import primepi


def fillPrimes(chprime, high):
    ck = [True] * (high + 1)

    l = int(math.sqrt(high))
    for i in range(2, l + 1):
        if ck[i]:
            for j in range(i * i, l + 1, i):
                ck[j] = False

    for k in range(2, l + 1):
        if ck[k]:
            chprime.append(k)


def segmentedSieve(low, high):
    chprime = list()
    fillPrimes(chprime, high)
    real_primes = []
    prime = [True] * (high - low + 1)
    for i in chprime:
        lower = (low // i)
        if lower <= 1:
            lower = i + i
        elif (low % i) != 0:
            lower = (lower * i) + i
        else:
            lower = lower * i
        for j in range(lower, high + 1, i):
            prime[j - low] = False

    for k in range(low, high + 1):
        if prime[k - low]:
            real_primes.append(k)
    return  real_primes
