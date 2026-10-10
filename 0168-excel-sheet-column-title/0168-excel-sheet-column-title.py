class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        result = []
        
        while columnNumber > 0:
            # Adjust columnNumber to 0-indexed (0 corresponds to 'A')
            columnNumber -= 1
            remainder = columnNumber % 26
            
            # Map remainder to character ('A' is ASCII 65)
            result.append(chr(ord('A') + remainder))
            
            columnNumber //= 26
            
        # Since we append from right to left, reverse the result array
        return "".join(result[::-1])