class Solution(object):
    def numPrimeArrangements(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10**9 + 7
        
        # Step 1: Count how many prime numbers exist between 1 and n
        def count_primes(num):
            if num < 2:
                return 0
            primes = [True] * (num + 1)
            primes[0] = primes[1] = False
            for i in range(2, int(num**0.5) + 1):
                if primes[i]:
                    for j in range(i*i, num + 1, i):
                        primes[j] = False
            return sum(primes)
            
        prime_count = count_primes(n)
        composite_count = n - prime_count
        
        # Step 2: Calculate factorials for prime positions and composite positions
        def factorial(num):
            res = 1
            for i in range(2, num + 1):
                res = (res * i) % MOD
            return res
            
        # Step 3: Total permutations are (prime_count!) * (composite_count!) % MOD
        return (factorial(prime_count) * factorial(composite_count)) % MOD