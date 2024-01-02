import segmented_sieve


def coprime(basis, turns):
    coprimes = []
    turn = 1
    remove = []
    for num in basis:
        turn *= num
    for i in range(3, turns * turn + 1, 2):
       coprimes.append(i)
    for coprime in coprimes:
        for prime in basis:
            if coprime % prime == 0:
                remove.append(coprime)
                break
    for error in remove:
        coprimes.remove(error)
    return coprimes, turn


basis = [2, 3, 5, 7, 11, 13]
turns = 1
primes, turn = coprime(basis, turns)
max = max(basis)
remove = []
for prime in primes:
    if prime >= max ** 2:
        remove.append(prime)
for error in remove:
    primes.remove(error)
primes_additive = segmented_sieve.segmentedSieve(max ** 2, turn * turns)
primes = basis + primes + primes_additive
print(primes)
print(len(primes))
