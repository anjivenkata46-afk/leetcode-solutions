class Solution(object):
    def findMin(self, nums):
        """:type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            # If the mid element is greater than the right element, 
            # the minimum must be in the right half.
            if nums[mid] > nums[right]:
                left = mid + 1
            # If the mid element is less than the right element, 
            # the minimum must be in the left half (including mid).
            elif nums[mid] < nums[right]:
                right = mid
            # When nums[mid] == nums[right], we can't be sure which side 
            # has the minimum, but we can safely decrement `right` to handle duplicates.
            else:
                right -= 1
                
        return nums[left]