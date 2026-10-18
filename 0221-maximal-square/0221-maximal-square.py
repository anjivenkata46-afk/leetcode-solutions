class Solution(object):
    def maximalSquare(self, matrix):
        """:type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        
        m, n = len(matrix), len(matrix[0])
        dp = [0] * (n + 1)
        max_side = 0
        prev = 0  # Represents dp[i-1][j-1]
        
        for i in range(m):
            for j in range(n):
                temp = dp[j + 1]
                if matrix[i][j] == '1':
                    # dp[j] is left, dp[j+1] is top, prev is top-left
                    dp[j + 1] = min(dp[j], dp[j + 1], prev) + 1
                    max_side = max(max_side, dp[j + 1])
                else:
                    dp[j + 1] = 0
                prev = temp
                
        return max_side * max_side