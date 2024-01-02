import time
import nth_prime
from sympy import primepi


def SieveOfSundaram(n):
    prime_list = [2]
    nNew = int((n - 1) / 2)
    marked = [0] * (nNew + 1)
    start_time = time.perf_counter_ns()
    for i in range(1, (nNew + 1)):
        j = i
        while (i + j + (2 * i * j)) <= nNew:
            marked[i + j + (2 * i * j)] = 1
            j += 1

    for i in range(1, nNew + 1):
        if marked[i] == 0:
            prime_list.append((2 * i + 1))
    end_time = time.perf_counter_ns()
    overall_time = end_time - start_time

    return overall_time

runs = 0
num_primes = 10
while runs < 100:
    start_time = time.perf_counter_ns()
    primes = nth_prime.nth_prime(num_primes)
    lower, upper = nth_prime.bounds(5000)
    previous = primepi(lower)
    num = primes[num_primes - previous - 1]
    SieveOfSundaram(num)
    end_time = time.perf_counter_ns()
    overall_time = end_time - start_time
    print(overall_time)
    runs += 1



