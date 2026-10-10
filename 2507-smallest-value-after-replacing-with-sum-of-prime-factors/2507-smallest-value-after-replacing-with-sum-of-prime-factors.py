class Solution(object):
    def smallestValue(self, n):
        """
        :type n: int
        :rtype: int
        """
        while True:
            current_sum = 0
            temp = n
            d = 2
            
            # Find all prime factors of temp and sum them
            while d * d <= temp:
                while temp % d == 0:
                    current_sum += d
                    temp //= d
                d += 1
            if temp > 1:
                current_sum += temp
                
            # If the sum equals n, n has stabilized to a prime or fixed point
            if current_sum == n:
                return n
                
            n = current_sum