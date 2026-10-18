class Solution(object):
    def summaryRanges(self, nums):
        """:type nums: List[int]
        :rtype: List[str]
        """
        res = []
        i = 0
        n = len(nums)
        
        while i < n:
            start = nums[i]
            j = i
            
            # Find the end of the consecutive range
            while j + 1 < n and nums[j + 1] == nums[j] + 1:
                j += 1
                
            # If the start and end are the same
            if start == nums[j]:
                res.append(str(start))
            else:
                res.append(str(start) + "->" + str(nums[j]))
                
            # Move to the next range
            i = j + 1
            
        return res