class Solution:
    def merge(self, intervals):
        intervals.sort()

        result = []

        for interval in intervals:
            start = interval[0]
            end = interval[1]

            if not result or start > result[-1][1]:
                result.append([start, end])
            else:
                result[-1][1] = max(result[-1][1], end)

        return result