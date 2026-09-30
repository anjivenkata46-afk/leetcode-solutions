class Solution:
    def permute(self, nums):
        result = []

        def backtrack(current):
            # If permutation is complete
            if len(current) == len(nums):
                result.append(current[:])
                return

            for num in nums:
                # Don't use the same number twice
                if num in current:
                    continue

                current.append(num)

                # Continue building permutation
                backtrack(current)

                # Remove last number
                current.pop()

        backtrack([])

        return result
        