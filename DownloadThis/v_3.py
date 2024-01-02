import time
import math


runs = 0
while runs < 100:
    num_primes = 10
    prime_list = [2, 3, 5]
    primes = 3
    start_time = time.perf_counter_ns()
    while primes < num_primes:
        for i in range(7, (2 ** num_primes), 2):
            sum = 0
            limit = math.ceil(math.sqrt(i + 1))
            last_digit = int(repr(i)[-1])
            for prime in prime_list:
                if prime >= limit:
                    break
                if last_digit == 5:
                    sum += 1
                    break
                if i % prime == 0:
                    sum += 1
            if sum == 0:
                prime_list.append(i)
                primes += 1
            if len(prime_list) == num_primes:
                break
    end_time = time.perf_counter_ns()
    overall_time = end_time - start_time
    print(overall_time)
    runs += 1
