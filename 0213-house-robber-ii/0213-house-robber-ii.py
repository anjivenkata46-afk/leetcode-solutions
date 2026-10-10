class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
            
        def rob_linear(houses):
            prev1 = 0
            prev2 = 0
            for num in houses:
                current = max(prev1, prev2 + num)
                prev2 = prev1
                prev1 = current
            return prev1
            
        # Since the first and last houses are connected in a circle, 
        # we cannot rob both. Therefore, we take the maximum of:
        # 1. Robbing from house 1 to the second-to-last house (excluding the last)
        # 2. Robbing from house 2 to the last house (excluding the first)
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))