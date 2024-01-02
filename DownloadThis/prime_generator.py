import segmented_sieve
import nth_prime
import time
import re
from math import floor


block = 0
num_primes = int(input('Number of primes to generate: '))
runs = 1
if num_primes >= 10000000:
    runs = floor(num_primes / 10000000)
    while block < runs:
        f = open('primes.txt', 'r+')
        start_time = time.perf_counter_ns()
        lines = f.readlines()
        primes = len(lines) - 1
        computing_line = lines[0]
        computing_time_current = re.findall(r'\d+', computing_line)
        f.close()
        f = open('primes.txt', 'r+')
        start = int(f.readlines()[-1]) + 1
        if (num_primes + primes) % 2 != 0:
            num_primes += 1
        stop = nth_prime.nth_prime(((block + 1) * 10000000) + primes + 2)[0]
        primes = segmented_sieve.segmentedSieve(start, stop)
        for prime in primes:
            f.write('\n')
            f.write(str(prime))
        computing_time_decimal = '0' + '.' + computing_time_current[1]
        computing_time_decimal = float(computing_time_decimal)
        computing_time_overall = float(computing_time_current[0]) + ((time.perf_counter_ns() - start_time) / 1000000000) + computing_time_decimal
        f.close()
        f = open('primes.txt', 'r+')
        data = f.readlines()
        data[0] = f'Computing Time: {computing_time_overall} seconds\n'
        f.seek(0)
        f.truncate()
        f.writelines(data)
        block += 1
    f = open('primes.txt', 'r+')
    start_time = time.perf_counter_ns()
    lines = f.readlines()
    primes = len(lines) - 1
    computing_line = lines[0]
    computing_time_current = re.findall(r'\d+', computing_line)
    f.close()
    f = open('primes.txt', 'r+')
    start = int(f.readlines()[-1]) + 1
    if (num_primes + primes) % 2 != 0:
        num_primes += 1
    stop = nth_prime.nth_prime((num_primes % 10000000) + primes + 2)[0]
    primes = segmented_sieve.segmentedSieve(start, stop)
    for prime in primes:
        f.write('\n')
        f.write(str(prime))
    computing_time_decimal = '0' + '.' + computing_time_current[1]
    computing_time_decimal = float(computing_time_decimal)
    computing_time_overall = float(computing_time_current[0]) + (
                (time.perf_counter_ns() - start_time) / 1000000000) + computing_time_decimal
    f.close()
    f = open('primes.txt', 'r+')
    data = f.readlines()
    data[0] = f'Computing Time: {computing_time_overall} seconds\n'
    f.seek(0)
    f.truncate()
    f.writelines(data)

else:
    f = open('primes.txt', 'r+')
    start_time = time.perf_counter_ns()
    lines = f.readlines()
    primes = len(lines) - 1
    computing_line = lines[0]
    computing_time_current = re.findall(r'\d+', computing_line)
    f.close()
    f = open('primes.txt', 'r+')
    start = int(f.readlines()[-1]) + 1
    if (num_primes + primes) % 2 != 0:
        num_primes += 1
    stop = nth_prime.nth_prime((num_primes % 10000000) + primes + 2)[0]
    primes = segmented_sieve.segmentedSieve(start, stop)
    for prime in primes:
        f.write('\n')
        f.write(str(prime))
    computing_time_decimal = '0' + '.' + computing_time_current[1]
    computing_time_decimal = float(computing_time_decimal)
    computing_time_overall = float(computing_time_current[0]) + ((time.perf_counter_ns() - start_time) / 1000000000) + computing_time_decimal
    f.close()
    f = open('primes.txt', 'r+')
    data = f.readlines()
    data[0] = f'Computing Time: {computing_time_overall} seconds\n'
    f.seek(0)
    f.truncate()
    f.writelines(data)