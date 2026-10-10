import functools

class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        # Convert all integers to strings
        str_nums = list(map(str, nums))
        
        # Custom comparator: if x + y > y + x, then x should come before y
        def compare(x, y):
            if x + y > y + x:
                return -1
            elif x + y < y + x:
                return 1
            else:
                return 0
                
        str_nums.sort(key=functools.cmp_to_key(compare))
        
        # Join the sorted strings
        result = "".join(str_nums)
        
        # Edge case: if the result starts with '0', the array only contained zeros (e.g., [0, 0])
        return "0" if result[0] == '0' else result