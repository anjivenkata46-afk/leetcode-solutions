class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        seen = {}
        for i, num in enumerate(nums):
            # If the number exists and the absolute difference between indices is <= k
            if num in seen and i - seen[num] <= k:
                return True
            # Update the last seen index of the number
            seen[num] = i
        return False