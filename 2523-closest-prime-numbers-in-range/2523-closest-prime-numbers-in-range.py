class Solution(object):
    def closestPrimes(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        # Step 1: Use Sieve of Eratosthenes to find all primes up to right
        is_prime = [True] * (right + 1)
        is_prime[0] = is_prime[1] = False
        
        for i in range(2, int(right**0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, right + 1, i):
                    is_prime[j] = False
                    
        # Step 2: Collect all prime numbers within the given [left, right] range
        primes = [i for i in range(left, right + 1) if is_prime[i]]
        
        # If there are fewer than 2 primes, no valid pair can be formed
        if len(primes) < 2:
            return [-1, -1]
            
        # Step 3: Find the pair with the minimum difference
        min_diff = float('inf')
        ans = [-1, -1]
        
        for i in range(len(primes) - 1):
            diff = primes[i + 1] - primes[i]
            if diff < min_diff:
                min_diff = diff
                ans = [primes[i], primes[i + 1]]
                
        return ans