class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):
        """
        :type nums: List[int]
        :type indexDiff: int
        :type valueDiff: int
        :rtype: bool
        """
        if valueDiff < 0:
            return False
            
        bucket_size = valueDiff + 1
        buckets = {}
        
        for i, num in enumerate(nums):
            # Determine the bucket ID for the current number
            bucket_id = num // bucket_size
            
            # Check if the exact bucket already contains a number
            if bucket_id in buckets:
                return True
                
            # Check the neighboring buckets for numbers within the valueDiff range
            if bucket_id - 1 in buckets and abs(num - buckets[bucket_id - 1]) <= valueDiff:
                return True
            if bucket_id + 1 in buckets and abs(num - buckets[bucket_id + 1]) <= valueDiff:
                return True
                
            # Put the current number into its bucket
            buckets[bucket_id] = num
            
            # Maintain the sliding window of size indexDiff by removing old elements
            if i >= indexDiff:
                old_bucket_id = nums[i - indexDiff] // bucket_size
                del buckets[old_bucket_id]
                
        return False