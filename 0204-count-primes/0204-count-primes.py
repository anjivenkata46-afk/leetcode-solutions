class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
            
        # Initialize a boolean list representing primality for numbers up to n-1
        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime numbers
        
        # Iterate from 2 up to the square root of n
        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:
                # Mark all multiples of i starting from i*i as False (not prime)
                is_prime[i * i : n : i] = [False] * len(range(i * i, n, i))
                
        return sum(is_prime)