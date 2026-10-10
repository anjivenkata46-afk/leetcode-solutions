class Solution(object):
    def findMin(self, nums):
        """:type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            # If the middle element is greater than the right-most element, 
            # the minimum must be in the right half.
            if nums[mid] > nums[right]:
                left = mid + 1
            # Otherwise, the minimum is in the left half (including mid).
            else:
                right = mid
                
        return nums[left]