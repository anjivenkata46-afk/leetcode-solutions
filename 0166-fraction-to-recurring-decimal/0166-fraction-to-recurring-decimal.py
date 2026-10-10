class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator == 0:
            return "0"
        
        result = []
        
        # Handle sign for negative fractions
        if (numerator < 0) ^ (denominator < 0):
            result.append('-')
            
        numerator = abs(numerator)
        denominator = abs(denominator)
        
        # Append the integer part
        result.append(str(numerator // denominator))
        remainder = numerator % denominator
        
        if remainder == 0:
            return "".join(result)
            
        # Append the decimal point
        result.append('.')
        
        # Map to store the remainder and its position in the result list
        remainder_map = {}
        
        while remainder != 0:
            if remainder in remainder_map:
                # Insert parentheses around the repeating part
                result.insert(remainder_map[remainder], '(')
                result.append(')')
                break
                
            # Record the index of the current remainder
            remainder_map[remainder] = len(result)
            
            remainder *= 10
            result.append(str(remainder // denominator))
            remainder %= denominator
            
        return "".join(result)