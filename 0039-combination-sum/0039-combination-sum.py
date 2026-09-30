class Solution:
    def combinationSum(self, candidates, target):
        result = []

        def backtrack(start, current, total):
            # Target reached
            if total == target:
                result.append(current[:])
                return

            # Sum exceeded target
            if total > target:
                return

            for i in range(start, len(candidates)):
                num = candidates[i]

                current.append(num)

                # i instead of i + 1 because
                # the same number can be used again
                backtrack(i, current, total + num)

                # Remove the number (backtrack)
                current.pop()

        backtrack(0, [], 0)

        return result