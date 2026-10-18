class Solution(object):
    def countDigitOne(self, n):
        """:type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
            
        count = 0
        divider = 1
        
        while divider <= n:
            lower = n - (n // divider) * divider
            curr = (n // divider) % 10
            higher = n // (divider * 10)
            
            if curr == 0:
                count += higher * divider
            elif curr == 1:
                count += higher * divider + (lower + 1)
            else:
                count += (higher + 1) * divider
                
            divider *= 10
            
        return count