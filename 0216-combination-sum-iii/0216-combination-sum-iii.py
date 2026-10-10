class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        result = []
        
        def backtrack(start, current_comb, current_sum):
            # Base case: if the combination has k elements and the sum matches n
            if len(current_comb) == k:
                if current_sum == n:
                    result.append(list(current_comb))
                return
            
            # Pruning: if current sum exceeds n, or we don't have enough numbers left to reach length k
            if current_sum > n or len(current_comb) + (10 - start) < k:
                return
                
            # Iterate through available numbers from start to 9
            for i in range(start, 10):
                current_comb.append(i)
                backtrack(i + 1, current_comb, current_sum + i)
                current_comb.pop() # Backtrack
                
        backtrack(1, [], 0)
        return result