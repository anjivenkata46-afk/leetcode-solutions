class Solution:
    def insert(self, intervals, newInterval):
        result = []

        start = newInterval[0]
        end = newInterval[1]

        for interval in intervals:
            # Current interval is completely before newInterval
            if interval[1] < start:
                result.append(interval)

            # Current interval is completely after newInterval
            elif interval[0] > end:
                result.append([start, end])
                start = interval[0]
                end = interval[1]

            # Overlapping intervals
            else:
                start = min(start, interval[0])
                end = max(end, interval[1])

        # Add newInterval
        result.append([start, end])

        return result