class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        # True if i is a prime number. Assume all are primes.
        sieve = [True] * n
        sieve[0] = False
        sieve[1] = False

        for i in range(0, int(sqrt(n) + 1)):
            if sieve[i]:
                # mark every multiple True
                for j in range(i * i, n, i):
                    sieve[j] = False
        return sum(sieve)