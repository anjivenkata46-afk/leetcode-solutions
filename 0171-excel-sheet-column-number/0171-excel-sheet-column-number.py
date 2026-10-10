class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        result = 0
        
        for char in columnTitle:
            # Shift existing result left by 26 and add the value of the current character
            result = result * 26 + (ord(char) - ord('A') + 1)
            
        return result