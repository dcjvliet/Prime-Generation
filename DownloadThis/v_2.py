import time


runs = 0
while runs < 100:
    num_primes = 100
    prime_list = [2, 3]
    primes = 2
    start_time = time.perf_counter_ns()
    while primes < num_primes:
        for i in range(5, (2 ** num_primes)):
            sum = 0
            for prime in prime_list:
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
