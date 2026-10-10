class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        if not dungeon or not dungeon[0]:
            return 0
            
        m = len(dungeon)
        n = len(dungeon[0])
        
        # DP table initialized with infinity, plus an extra row and column as padding
        dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]
        
        # Base cases for the cells just outside the bottom-right corner
        dp[m][n - 1] = 1
        dp[m - 1][n] = 1
        
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                # Minimum health needed from right or down choices
                min_health_on_exit = min(dp[i + 1][j], dp[i][j + 1])
                
                # Calculate needed health entering current room, ensuring it's at least 1
                dp[i][j] = max(1, min_health_on_exit - dungeon[i][j])
                
        return dp[0][0]