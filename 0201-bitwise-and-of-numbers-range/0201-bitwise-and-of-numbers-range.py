class Solution(object):
    def rangeBitwiseAnd(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        shift = 0
        # Find the common prefix of left and right by shifting right
        while left < right:
            left >>= 1
            right >>= 1
            shift += 1
            
        # Shift back to the left by the number of shifts we performed
        return left << shift