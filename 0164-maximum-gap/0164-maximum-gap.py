class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) < 2:
            return 0
        
        n = len(nums)
        min_val = min(nums)
        max_val = max(nums)
        
        # Edge case: all elements are the same
        if min_val == max_val:
            return 0
        
        # Calculate minimum possible gap and bucket size
        # Using ceiling division: bucket_size = ceil((max_val - min_val) / (n - 1))
        bucket_size = max(1, (max_val - min_val) // (n - 1))
        bucket_count = (max_val - min_val) // bucket_size + 1
        
        # Initialize buckets to store the minimum and maximum values in each bucket
        bucket_min = [float('inf')] * bucket_count
        bucket_max = [float('-inf')] * bucket_count
        
        # Distribute numbers into buckets
        for num in nums:
            idx = (num - min_val) // bucket_size
            bucket_min[idx] = min(bucket_min[idx], num)
            bucket_max[idx] = max(bucket_max[idx], num)
            
        # Scan buckets to find the maximum gap
        max_gap = 0
        prev_max = min_val
        
        for i in range(bucket_count):
            # Skip empty buckets
            if bucket_min[i] == float('inf'):
                continue
            
            # The gap is between the current bucket's minimum and the previous non-empty bucket's maximum
            max_gap = max(max_gap, bucket_min[i] - prev_max)
            prev_max = bucket_max[i]
            
        return max_gap