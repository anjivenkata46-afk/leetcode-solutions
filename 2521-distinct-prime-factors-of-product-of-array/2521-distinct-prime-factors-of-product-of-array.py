class Solution(object):
    def distinctPrimeFactors(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        distinct_primes = set()
        
        for num in nums:
            d = 2
            # Find prime factors of each number using trial division
            while d * d <= num:
                while num % d == 0:
                    distinct_primes.add(d)
                    num //= d
                d += 1
            if num > 1:
                distinct_primes.add(num)
                
        return len(distinct_primes)