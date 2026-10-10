class Solution:
    def minCut(self, s):
        n = len(s)
        dp = list(range(n))

        for i in range(n):
            # Odd-length palindromes
            left = right = i
            while left >= 0 and right < n and s[left] == s[right]:
                if left == 0:
                    dp[right] = 0
                else:
                    dp[right] = min(dp[right], dp[left - 1] + 1)

                left -= 1
                right += 1

            # Even-length palindromes
            left, right = i, i + 1
            while left >= 0 and right < n and s[left] == s[right]:
                if left == 0:
                    dp[right] = 0
                else:
                    dp[right] = min(dp[right], dp[left - 1] + 1)

                left -= 1
                right += 1

        return dp[n - 1]